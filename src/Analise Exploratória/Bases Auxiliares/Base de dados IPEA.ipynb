import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Inserção dos dados
dados_anuais = {
    "Atributo": [
        "Rendimento médio real (todos trabalhos)",
        "Média horas (trabalho principal - efetivo)",
        "Média horas (trabalho principal - habitual)",
        "Média horas (todos trabalhos - efetivo)",
        "Média horas (todos trabalhos - habitual)",
        "Informalidade",
        "Força de trabalho",
        "Ocupados",
        "Desocupados",
        "Fora da força de trabalho",
        "Rendimento (trabalho principal - efetivo)",
        "Rendimento (trabalho principal - habitual)",
        "Rendimento (todos trabalhos - habitual)",
        "Taxa de participação",
        "Taxa de desemprego"
    ],
    "Unidade": [
        "R$", "horas", "horas", "horas", "horas", "%", 
        "milhões", "milhões", "milhões", "milhões", 
        "R$", "R$", "R$", "%", "%"
    ],
    "2018": [
        3749.25, 34.38, 36.35, 34.80, 36.80, 57.33,
        6.25, 6.85, 2.23, 34.80, 3578.00, 3629.00, 3752.00, 23.63, 4.40
    ],
    "2019": [
        3690.75, 34.28, 36.10, 34.68, 36.58, 57.08,
        6.53, 7.08, 2.50, 35.98, 3551.00, 3586.00, 3696.00, 24.05, 4.55
    ],
    "2020": [
        972.00, 8.03, 9.03, 8.10, 9.13, 52.10,
        6.23, 6.85, 2.23, 34.48, 3783.00, 3586.00, 3700.00, 20.85, 4.93
    ],
    "2021": [
        0.00, 0.00, 0.00, 0.00, 0.00, 53.88,
        6.23, 6.80, 2.53, 37.13, 0.00, 0.00, 0.00, 21.05, 5.33
    ],
    "2022": [
        2637.75, 34.65, 36.38, 34.83, 36.75, 55.15,
        6.85, 7.28, 2.85, 38.30, 3279.00, 3277.00, 3384.00, 22.93, 4.00
    ],
    "2023": [
        2821.31, 34.65, 36.28, 34.78, 36.70, 54.93,
        7.33, 7.65, 3.23, 38.43, 3691.00, 3490.00, 3586.00, 23.55, 3.50
    ]
}

df_anual = pd.DataFrame(dados_anuais).melt(
    id_vars=["Atributo", "Unidade"], 
    var_name="Ano", 
    value_name="Média"
)

plt.figure(figsize=(18, 10))
sns.set_theme(style="whitegrid")

ax = sns.barplot(
    data=df_anual,
    x="Atributo",
    y="Média",
    hue="Ano",
    palette="viridis",
    errorbar=None
)

plt.title("Comparação Anual de Indicadores Trabalhistas para Pessoas com 60+ Anos (2018-2023)", fontsize=14, pad=20)
plt.xlabel("Atributo", fontsize=12)
plt.ylabel("Média Anual", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title="Ano", bbox_to_anchor=(1.05, 1), loc='upper left')

for p in ax.patches:
    if p.get_height() > 0: 
        ax.annotate(
            f"{p.get_height():.1f}", 
            (p.get_x() + p.get_width() / 2., p.get_height()), 
            ha='center', va='center', 
            xytext=(0, 5), 
            textcoords='offset points',
            fontsize=8,
            rotation=90
        )

plt.tight_layout()
plt.show()


