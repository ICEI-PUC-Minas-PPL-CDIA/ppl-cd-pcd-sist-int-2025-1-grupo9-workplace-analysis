import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

sns.set(style="whitegrid")

#PRIMEIRO GRÁFICO
valores_ocupacao = [17.8, 17.9, 9.9, 44.4, 7.9, 2.1]
labels = [
    "Com carteira assinada",
    "Sem carteira assinada",
    "Militar/função pública",
    "Conta própria",
    "Empregador",
    "Omissos"
]

plt.figure(figsize=(8, 8))
plt.pie(valores_ocupacao, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Distribuição percentual por ocupação 55+", fontsize=14, pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()

#SEGUNDO GRÁFICO
grupos_atividade = [
    "Total", "Agropecuária", "Indústria", "Construção", 
    "Comércio e reparação", "Adm. pública, educação, saúde e serv. sociais",
    "Transporte, armazenagem e correio", "Alojamento e alimentação",
    "Informação, financeira e outras ativ. profissionais", "Serviços domésticos",
    "Outros serviços"
]
pessoas_ocupadas = [
    100690, 8146, 12904, 7431, 
    19034, 17928, 5503, 5567, 
    12614, 6104, 5418
]

df = pd.DataFrame({
    "Grupo de Atividade": grupos_atividade,
    "Pessoas Ocupadas (1 000)": pessoas_ocupadas
})
df["Pessoas Ajustadas"] = df["Pessoas Ocupadas (1 000)"].apply(lambda x: math.floor(x * 0.19))

plt.figure(figsize=(12, 6))
ax = sns.lineplot(
    data=df,
    x="Grupo de Atividade",
    y="Pessoas Ajustadas",
    marker="o",
    markersize=8,
    linewidth=2.5,
    color="blue"
)

for i, valor in enumerate(df["Pessoas Ajustadas"]):
    ax.text(
        i,
        valor,
        f"{valor}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.title("Pessoas +60 anos por Grupo de Atividade", fontsize=14, pad=20)
plt.xlabel("Grupo de Atividade", labelpad=10)
plt.ylabel("Número de Pessoas (1 000, ajustado)", labelpad=10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
