import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados simulados para profissionais 55+ com base na descrição fornecida
np.random.seed(42)
n = 300
df = pd.DataFrame({
    "Idade": np.random.randint(55, 75, n),
    "Faixa etária": ["55+"] * n,
    "Gênero": np.random.choice(["Masculino", "Feminino", "Não-binário"], n),
    "Área de atuação profissional": np.random.choice(
        ["Ciência de Dados", "Análise de Dados", "Engenharia", "RH", "Financeiro"], n),
    "Tipo de empresa": np.random.choice(["Pública", "Privada", "Startup", "Autônomo"], n),
    "Salário (faixa ou média)": np.random.normal(8000, 2000, n).round(0),
    "Satisfação profissional": np.random.choice(["Baixo", "Médio", "Alto"], n),
    "Já sofreu discriminação por idade?": np.random.choice(["Sim", "Não"], n, p=[0.3, 0.7]),
    "Adequação às novas tecnologias": np.random.choice(["Nenhuma", "Pouca", "Média", "Alta"], n)
})

# Ordenação de variáveis ordinais
ordem_satisfacao = {"Baixo": 1, "Médio": 2, "Alto": 3}
ordem_tecnologia = {"Nenhuma": 0, "Pouca": 1, "Média": 2, "Alta": 3}
df["Satisfação profissional (n)"] = df["Satisfação profissional"].map(ordem_satisfacao)
df["Adequação às novas tecnologias (n)"] = df["Adequação às novas tecnologias"].map(ordem_tecnologia)

plt.figure(figsize=(10,6))
sns.countplot(data=df, y="Área de atuação profissional", 
              order=df["Área de atuação profissional"].value_counts().index)
plt.title('Profissionais 55+ por Área de Atuação')
plt.xlabel('Número de Pessoas')
plt.ylabel('Área de Atuação')
plt.tight_layout()
plt.show()

discrim_counts = df["Já sofreu discriminação por idade?"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(discrim_counts, labels=discrim_counts.index, autopct='%1.1f%%', startangle=140, 
        colors=['#ff9999','#66b3ff'])
plt.title('Discriminação por Idade - Profissionais 55+')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="Tipo de empresa", y="Satisfação profissional (n)")
plt.title('Satisfação Profissional por Tipo de Empresa - 55+')
plt.xlabel('Tipo de Empresa')
plt.ylabel('Satisfação (Escala Ordinal)')
plt.tight_layout()
plt.show()

df_dados = df[df["Área de atuação profissional"].str.contains("Dados")]

plt.figure(figsize=(10,6))
sns.barplot(data=df_dados, x="Área de atuação profissional", y="Salário (faixa ou média)", 
            estimator=np.mean, ci=None)
plt.title('Salário Médio - Área de Dados - Profissionais 55+')
plt.ylabel('Salário (R$)')
plt.xlabel('Área de Atuação')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Idade", y="Adequação às novas tecnologias (n)", 
                hue="Área de atuação profissional")
plt.title('Idade vs Adequação às Novas Tecnologias - Profissionais 55+')
plt.xlabel('Idade')
plt.ylabel('Adequação (0 = Nenhuma, 3 = Alta)')
plt.tight_layout()
plt.show()

num_df = df[["Idade", "Salário (faixa ou média)", "Satisfação profissional (n)", 
             "Adequação às novas tecnologias (n)"]]

plt.figure(figsize=(10,8))
sns.heatmap(num_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Correlação - Variáveis Numéricas (55+)')
plt.tight_layout()
plt.show()

