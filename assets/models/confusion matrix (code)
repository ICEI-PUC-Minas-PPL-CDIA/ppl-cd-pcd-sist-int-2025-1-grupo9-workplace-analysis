# Imports necessários
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from imblearn.over_sampling import SMOTE

# Leitura da base
df = pd.read_excel("base_unificada_limpa.xlsx")  # mesmo nome de arquivo usado no modelo

# Criação do grupo etário e variável alvo
df['grupo_etário'] = df['idade'].apply(lambda x: '50+' if x >= 50 else '<50')
df['etarismo'] = df['experiência_prejudicada'].apply(
    lambda x: 1 if isinstance(x, str) and 'idade' in x.lower() else 0
)

# Features usadas no modelo
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

# Codificar variáveis categóricas
for col in X.select_dtypes(include='object').columns:
    X[col] = LabelEncoder().fit_transform(X[col])

# Aplicar SMOTE para balanceamento
X_bal, y_bal = SMOTE(random_state=42).fit_resample(X, y)

# Separar treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.3, random_state=42)

# Modelo Random Forest com os mesmos parâmetros
rf = RandomForestClassifier(n_estimators=200, max_depth=12, min_samples_split=5, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_matrix,
                       index=["Real Sem Etarismo", "Real Com Etarismo"],
                       columns=["Previsto Sem Etarismo", "Previsto Com Etarismo"])

# Impressões
print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}")
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))
print("\nMatriz de Confusão:")
print(conf_df)

# Visualização gráfica da matriz
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=["Sem Etarismo", "Com Etarismo"],
            yticklabels=["Sem Etarismo", "Com Etarismo"])
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão - Random Forest")
plt.tight_layout()
plt.show()
