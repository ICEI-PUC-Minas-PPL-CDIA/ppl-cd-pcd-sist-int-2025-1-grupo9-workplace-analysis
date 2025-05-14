import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("base_unificada_limpa.csv")

#Remoção dos atributos que bugaram
colunas_remover = [
    "rendimento médio 60+", 
    "participação no mercado 60+", 
    "taxa de desemprego 60+"
]

df = df.drop(columns=colunas_remover, errors='ignore')
df = df.drop(columns=df.filter(like='60+').columns, errors='ignore')
df = df.drop(columns=df.filter(regex='60\+').columns, errors='ignore')

df_numerico = df.select_dtypes(include=["int64", "float64"])
df_numerico = df_numerico.dropna(axis=1, thresh=int(len(df_numerico)*0.8))

plt.figure(figsize=(14,12))
sns.heatmap(
    df_numerico.corr().abs(),
    annot=True,
    fmt=".2f",
    cmap="Blues",
    vmin=0,
    vmax=1,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8},
    annot_kws={"size": 10}
)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.title("Matriz de Confusão", fontsize=14) 
plt.tight_layout()
plt.show()
