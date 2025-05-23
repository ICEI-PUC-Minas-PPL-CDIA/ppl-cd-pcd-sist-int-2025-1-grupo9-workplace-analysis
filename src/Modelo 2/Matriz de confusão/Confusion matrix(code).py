!pip install -U imbalanced-learn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
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

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=["Previsto: Não", "Previsto: Sim"],
            yticklabels=["Real: Não", "Real: Sim"])

plt.title("Matriz de Confusão - KNN (k=3)")
plt.xlabel("Classe Prevista")
plt.ylabel("Classe Real")
plt.tight_layout()
plt.show()
