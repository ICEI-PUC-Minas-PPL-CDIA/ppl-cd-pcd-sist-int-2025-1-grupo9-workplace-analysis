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

uploaded = files.upload()
df = pd.read_excel(next(iter(uploaded)))

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

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

for k in range(1, 11):
    print(f"\nAvaliando K = {k}")
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"Acurácia: {acc:.4f}")
    print(f"Precisão: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1-score: {f1:.4f}")
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
