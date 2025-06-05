import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifierAdd commentMore actions
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE

df = pd.read_csv('base_unificada_limpa.csv')

#Criação de variáveis
df['grupo_etário'] = df['idade'].apply(lambda x: '50+' if x >= 50 else '<50')
df['etarismo'] = df['experiência_prejudicada'].apply(
    lambda x: 1 if isinstance(x, str) and 'idade' in x.lower() else 0
)

#Seleção de features
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

#Preparação dos dados
df_model = df[features + ['etarismo']].dropna()
X = df_model[features]
y = df_model['etarismo']

#Codificação de variáveis categóricas
for col in X.select_dtypes(include='object').columns:
    X[col] = LabelEncoder().fit_transform(X[col])

#Balanceamento com SMOTE
smote = SMOTE(random_state=42)
X_bal, y_bal = smote.fit_resample(X, y)

#Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.3, random_state=42)

#Treinamento do modelo
rf = RandomForestClassifier(n_estimators=200, max_depth=12, min_samples_split=5, random_state=42)
rf.fit(X_train, y_train)

#Acurácia no conjunto de treino
train_pred = rf.predict(X_train)
acc_train = accuracy_score(y_train, train_pred)

#Acurácia no conjunto de teste
test_pred = rf.predict(X_test)
acc_test = accuracy_score(y_test, test_pred)

#Gráfico de comparação
plt.figure(figsize=(6, 4))
plt.bar(['Treinamento', 'Teste'], [acc_train, acc_test])
plt.title('Comparação de Acurácia - Random Forest')
plt.ylabel('Acurácia')
plt.ylim(0, 1)
for i, acc in enumerate([acc_train, acc_test]):
    plt.text(i, acc + 0.02, f'{acc:.2f}', ha='center')
plt.tight_layout()
plt.show()
