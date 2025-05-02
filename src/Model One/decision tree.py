import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Simulação de dados baseados no dicionário da base unificada (por falta de acesso direto ao DataFrame original)
np.random.seed(42)
n = 500

df = pd.DataFrame({
    "Idade": np.random.randint(55, 75, size=n),
    "Escolaridade (n)": np.random.choice([1, 2, 3, 4], size=n),  # 1 = Graduação, ..., 4 = Doutorado
    "Modelo de trabalho": np.random.choice(["Presencial", "Remoto", "Híbrido"], size=n),
    "Formalidade do emprego": np.random.choice(["Formal", "Informal"], size=n),
    "Acesso a treinamentos (n)": np.random.choice([0, 1, 2], size=n),  # 0 = Não, ..., 2 = Sim
    "Frequência de atualização profissional (n)": np.random.choice([0, 1, 2, 3], size=n),
    "Sentimento de valorização na empresa (n)": np.random.choice([1, 2, 3, 4, 5], size=n)
})

# Conversão de categóricas para dummies
df = pd.get_dummies(df, columns=["Modelo de trabalho", "Formalidade do emprego"], drop_first=True)

# Separando variáveis
X = df.drop(columns=["Sentimento de valorização na empresa (n)"])
y = df["Sentimento de valorização na empresa (n)"]

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do modelo (árvore de regressão para valor ordinal)
model = DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Predição e métricas
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Visualização da árvore
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True)
plt.title("Árvore de Decisão - Predição do Sentimento de Valorização (55+)")
plt.show()

(mae, rmse, r2)
