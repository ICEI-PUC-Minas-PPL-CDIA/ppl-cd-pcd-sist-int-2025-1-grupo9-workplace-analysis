import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # estilo visual dos gráficos

np.random.seed(42)
n = 300  # número de registros simulados

# Simulação dos dados
df = pd.DataFrame({
    "Idade": np.random.randint(55, 75, n),
    "Faixa etária": ["55+"] * n,
    "Gênero": np.random.choice(["Masculino", "Feminino", "Não-binário"], n),
    "Cor/Raça/Etnia": np.random.choice(["Branca", "Preta", "Parda", "Amarela", "Indígena"], n),
    "Área de atuação": np.random.choice(["Ciência de Dados", "Análise de Dados", "Engenharia", "RH", "Financeiro"], n),
    "Tipo de empresa": np.random.choice(["Pública", "Privada", "Startup", "Autônomo"], n),
    "Modelo de trabalho": np.random.choice(["Presencial", "Híbrido", "Remoto"], n),
    "Nível de escolaridade": np.random.choice(["Graduação", "Pós-graduação", "Mestrado", "Doutorado"], n),
    "Salário": np.random.normal(8000, 2000, n).round(0),
    "Satisfação profissional": np.random.choice(["Baixo", "Médio", "Alto"], n),
    "Já sofreu discriminação por idade?": np.random.choice(["Sim", "Não"], n, p=[0.3, 0.7]),
    "Adequação às novas tecnologias": np.random.choice(["Nenhuma", "Pouca", "Média", "Alta"], n),
    "Acesso a treinamentos e capacitações": np.random.choice(["Sim", "Não", "Ocasionalmente"], n),
    "Frequência de atualização profissional": np.random.choice(["Nunca", "Raramente", "Algumas vezes", "Frequentemente"], n),
    "Barreiras para recolocação profissional": np.random.choice(["Falta de oportunidades", "Exigência de tecnologia", "Salário abaixo do esperado"], n),
    "Sentimento de valorização na empresa": np.random.choice(["Muito baixo", "Baixo", "Médio", "Alto", "Muito alto"], n),
    "Oportunidades de promoção": np.random.choice(["Sim", "Não", "Raramente"], n)
})

# Mapeamento de variáveis ordinais
df["Satisfação profissional (n)"] = df["Satisfação profissional"].map({"Baixo": 1, "Médio": 2, "Alto": 3})
df["Valorização (n)"] = df["Sentimento de valorização na empresa"].map({
    "Muito baixo": 1, "Baixo": 2, "Médio": 3, "Alto": 4, "Muito alto": 5
})
df["Adequação às novas tecnologias (n)"] = df["Adequação às novas tecnologias"].map({
    "Nenhuma": 0, "Pouca": 1, "Média": 2, "Alta": 3
})

# Gráfico 1 - Escolaridade
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Nível de escolaridade", order=["Graduação", "Pós-graduação", "Mestrado", "Doutorado"])
plt.title("Nível de Escolaridade - Profissionais 55+")
plt.xlabel("Escolaridade")
plt.ylabel("Número de Pessoas")
plt.tight_layout()
plt.show()

# Gráfico 2 - Modelo de trabalho
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Modelo de trabalho", order=["Presencial", "Híbrido", "Remoto"])
plt.title("Modelo de Trabalho - Profissionais 55+")
plt.xlabel("Modelo")
plt.ylabel("Número de Pessoas")
plt.tight_layout()
plt.show()

# Gráfico 3 - Valorização x Escolaridade
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="Nível de escolaridade", y="Valorização (n)", order=["Graduação", "Pós-graduação", "Mestrado", "Doutorado"])
plt.title("Sentimento de Valorização por Escolaridade - Profissionais 55+")
plt.xlabel("Escolaridade")
plt.ylabel("Valorização (ordinal)")
plt.tight_layout()
plt.show()

# Gráfico 4 - Adequação tecnológica
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Adequação às novas tecnologias", order=["Nenhuma", "Pouca", "Média", "Alta"])
plt.title("Adequação às Novas Tecnologias - Profissionais 55+")
plt.xlabel("Nível de Adequação")
plt.ylabel("Número de Pessoas")
plt.tight_layout()
plt.show()

# Gráfico 5 - Atualização profissional
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Frequência de atualização profissional", order=["Nunca", "Raramente", "Algumas vezes", "Frequentemente"])
plt.title("Frequência de Atualização Profissional - Profissionais 55+")
plt.xlabel("Frequência")
plt.ylabel("Número de Pessoas")
plt.tight_layout()
plt.show()

# Gráfico 6 - Oportunidades de promoção
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Oportunidades de promoção", order=["Sim", "Raramente", "Não"])
plt.title("Percepção sobre Oportunidades de Promoção - Profissionais 55+")
plt.xlabel("Oportunidades")
plt.ylabel("Número de Pessoas")
plt.tight_layout()
plt.show()
