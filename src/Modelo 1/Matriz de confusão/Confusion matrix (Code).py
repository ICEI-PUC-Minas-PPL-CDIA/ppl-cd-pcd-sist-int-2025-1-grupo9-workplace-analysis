# Imports necessários
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from imblearn.over_sampling import SMOTE

# Leitura da base de dados
df = pd.read_csv("base_unificada_limpa.csv")

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

# Pré-processamento
df_model = df[features + ['etarismo']].dropna()
X = df_model[features]
y = df_model['etarismo']

for col in X.select_dtypes(include='object').columns:
    X[col] = LabelEncoder().fit_transform(X[col])

# Balanceamento com SMOTE
X_bal, y_bal = SMOTE(random_state=42).fit_resample(X, y)

# Divisão treino/teste (mesma divisão do modelo principal)
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.3, random_state=42)

# Otimização com GridSearchCV (se já executado anteriormente)
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

# Previsões com o modelo otimizado
y_pred = best_rf.predict(X_test)

# Avaliação
acc = accuracy_score(y_test, y_pred)
print(f"Acurácia: {acc:.4f}")

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_matrix,
                       index=["Real Sem Etarismo", "Real Com Etarismo"],
                       columns=["Previsto Sem Etarismo", "Previsto Com Etarismo"])

print("\nMatriz de Confusão:")
print(conf_df)

# Visualização da Matriz
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=["Sem Etarismo", "Com Etarismo"],
            yticklabels=["Sem Etarismo", "Com Etarismo"])
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão - Random Forest")
plt.tight_layout()
plt.show()
