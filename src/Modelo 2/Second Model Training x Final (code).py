!pip install -U imbalanced-learn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from imblearn.over_sampling import SMOTE
from google.colab import files

# Leitura
df = pd.read_csv('base_unificada_limpa.csv')

# Filtro e definição de variáveis
df_model = df[df['idade'] >= 50].copy()
target = 'já_sofreu_discriminação_por_idade?'

features = [
    'idade', 'faixa_etária', 'gênero', 'cor/raça/etnia', 'pcd',
    'anos_de_experiência', 'área_de_atuação', 'nível_de_escolaridade',
    'salário', 'tipo_de_empresa', 'tamanho_da_empresa',
    'satisfação_profissional', 'oportunidades_de_promoção',
    'adequação_às_novas_tecnologias',
    'incentivo_à_diversidade_etária_na_empresa',
    'planos_de_aposentadoria_e_transição_de_carreira'
]

df_model = df_model[features + [target]].dropna()
X = pd.get_dummies(df_model[features])
y = df_model[target]

# Balanceamento com SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Separação em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.3, random_state=42)

# Padronização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Armazenamento dos resultados
results = []

# Avaliação para K = 1 a 10
for k in range(1, 6):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    
    # Acurácia no treinamento
    y_train_pred = knn.predict(X_train_scaled)
    train_acc = accuracy_score(y_train, y_train_pred)

    # Acurácia no teste
    y_test_pred = knn.predict(X_test_scaled)
    test_acc = accuracy_score(y_test, y_test_pred)

    print(f"\nK = {k}")
    print(f"Acurácia de Treinamento: {train_acc:.4f}")
    print(f"Acurácia de Teste: {test_acc:.4f}")
    print("Matriz de Confusão (Teste):")
    print(confusion_matrix(y_test, y_test_pred))

    results.append({'K': k, 'Train Accuracy': train_acc, 'Test Accuracy': test_acc})

# Visualização
results_df = pd.DataFrame(results)
plt.figure(figsize=(10, 6))
plt.plot(results_df['K'], results_df['Train Accuracy'], label='Acurácia de Treinamento', marker='o')
plt.plot(results_df['K'], results_df['Final Accuracy'], label='Acurácia Final', marker='o')
plt.title('Comparação entre Acurácia de Treinamento e Final por K')
plt.xlabel('Valor de K')
plt.ylabel('Acurácia')
plt.legend()
plt.grid(True)
plt.show()
