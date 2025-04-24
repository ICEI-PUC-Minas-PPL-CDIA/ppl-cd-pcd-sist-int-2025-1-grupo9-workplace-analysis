# 1. Verificando valores ausentes
print(" Valores ausentes por coluna:")
print(df.isnull().sum())

# 2. Preenchendo ou removendo valores ausentes
# Exemplo: substituindo "Salário" ausente por mediana
if df["Salário"].isnull().sum() > 0:
    df["Salário"] = df["Salário"].fillna(df["Salário"].median())

# 3. Padronização de colunas categóricas
colunas_categoricas = [
    "Gênero", "Cor/Raça/Etnia", "Área de atuação profissional", "Tipo de empresa",
    "Modelo de trabalho", "Vínculo empregatício (classificação IBGE)", "Formalidade do emprego",
    "Já sofreu discriminação por idade?", "Tipo de discriminação por idade",
    "Motivo da experiência prejudicada", "Acesso a mentorias e suporte",
    "Flexibilidade no trabalho (55+)", "Incentivo à diversidade etária na empresa",
    "Planos de aposentadoria e transição de carreira"
]

for col in colunas_categoricas:
    df[col] = df[col].str.strip().str.title()

# 4. Conversão de variáveis ordinais para escala numérica
ordens = {
    "Escolaridade": {"Graduação": 1, "Pós-graduação": 2, "Mestrado": 3, "Doutorado": 4},
    "Satisfação profissional": {"Baixo": 1, "Médio": 2, "Alto": 3},
    "Adequação às novas tecnologias": {"Nenhuma": 0, "Pouca": 1, "Média": 2, "Alta": 3},
    "Acesso a treinamentos": {"Não": 0, "Ocasionalmente": 1, "Sim": 2},
    "Frequência de atualização profissional": {"Nunca": 0, "Raramente": 1, "Algumas vezes": 2, "Frequentemente": 3},
    "Sentimento de valorização na empresa (55+)": {
        "Muito baixo": 1, "Baixo": 2, "Médio": 3, "Alto": 4, "Muito alto": 5
    },
    "Oportunidades de promoção": {"Não": 0, "Raramente": 1, "Sim": 2}
}

for col, mapping in ordens.items():
    if col in df.columns:
        df[col + " (n)"] = df[col].map(mapping)

# 5. Remoção de outliers em "Salário"
q1 = df["Salário"].quantile(0.25)
q3 = df["Salário"].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

df = df[(df["Salário"] >= limite_inferior) & (df["Salário"] <= limite_superior)]

# 6. Resetando índice após limpeza
df.reset_index(drop=True, inplace=True)
