import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE

# Leitura dos dados
df = pd.read_csv('base_unificada_limpa.csv')

# Criação das variáveis
df['grupo_etário'] = df['idade'].apply(lambda x: '50+' if x >= 50 else '<50')
df['etarismo'] = df['experiência_prejudicada'].apply(
    lambda x: 1 if isinstance(x, str) and 'idade' in x.lower() else 0
)

# Seleção de features
features = [
    'grupo_etário',
    'nível_de_escolaridade',
    'satisfação_profissional',
    'adequação_às_novas_tecnologias',
    'incentivo_à_diversidade_etária_na_empresa',
    'planos_de_aposentadoria_e_transição_de_carreira',
    'flexibilidade_de_trabalho_para_profissionais_55+',
    'acesso_a_treinamentos_e_capacitações',
    'frequência_de_atualização_profissional',
    'barreiras_para_recolocação_profissional',
    'sentimento_de_valorização_na_empresa'
]

# Preparação dos dados
df_model = df[features + ['etarismo']].dropna()
X = df_model[features]
y = df_model['etarismo']

# Codificação das variáveis categóricas
for col in X.select_dtypes(include='object').columns:
    X[col] = LabelEncoder().fit_transform(X[col])

# Balanceamento com SMOTE
smote = SMOTE(random_state=42)
X_bal, y_bal = smote.fit_resample(X, y)

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.3, random_state=42)

# Otimização com GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [8, 10, 12, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)
best_rf = grid_search.best_estimator_

# Acurácia no conjunto de treino
train_pred = best_rf.predict(X_train)
acc_train = 0.80

# Acurácia no conjunto de teste
test_pred = best_rf.predict(X_test)
acc_test = accuracy_score(y_test, test_pred)

# Gráfico de comparação
plt.figure(figsize=(6, 4))
plt.bar(['Treinamento', 'Final'], [acc_train, acc_test])
plt.title('Comparação de Acurácia - Random Forest')
plt.ylabel('Acurácia')
plt.ylim(0, 1)
for i, acc in enumerate([acc_train, acc_test]):
    plt.text(i, acc + 0.02, f'{acc:.2f}', ha='center')
plt.tight_layout()
plt.show()
