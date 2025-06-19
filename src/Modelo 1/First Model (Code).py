# ETAPA 1: Instalação de pacotes no Colab
!pip install -U imbalanced-learn graphviz
!apt-get install -y graphviz

# ETAPA 2: Imports
import pandas as pd
import matplotlib.pyplot as plt
import graphviz
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree, export_graphviz
from imblearn.over_sampling import SMOTE
from google.colab import files

# ETAPA 3: Leitura dos dados
df = pd.read_csv("base_unificada_limpa.csv")

# ETAPA 4: Criação das variáveis
df['grupo_etário'] = df['idade'].apply(lambda x: '50+' if x >= 50 else '<50')
df['etarismo'] = df['experiência_prejudicada'].apply(
    lambda x: 1 if isinstance(x, str) and 'idade' in x.lower() else 0
)

features = [
    'grupo_etário',
    'nível_de_escolaridade',
    'satisfação_profissional',
    'adequação_às_novas_tecnologias',
    'incentivo_à_diversidade_etária_na_empresa',
    'planos_de_aposentadoria_e_transição_de_carreira',
    'flexibilidade_de_trabalho_para_profissionais_55+',
    'acesso_a_treinamentos_e_capacitações',
    'frequência_de_atualização_profissional',
    'barreiras_para_recolocação_profissional',
    'sentimento_de_valorização_na_empresa'
]

df_model = df[features + ['etarismo']].dropna()
X = df_model[features]
y = df_model['etarismo']

# ETAPA 5: Codificação
for col in X.select_dtypes(include='object').columns:
    X[col] = LabelEncoder().fit_transform(X[col])

# ETAPA 6: Balanceamento com SMOTE
X_bal, y_bal = SMOTE(random_state=42).fit_resample(X, y)

# ETAPA 7: Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.3, random_state=42)

# ETAPA 8: Otimização de Hiperparâmetros com GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [8, 10, 12, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

print("Melhores parâmetros encontrados:", grid_search.best_params_)

# ETAPA 9: Treinamento e Avaliação com o melhor modelo
best_rf = grid_search.best_estimator_
y_pred = best_rf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Acurácia: {acc:.4f}")
print(report)

conf_matrix = confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_matrix,
                       index=["Real Sem Etarismo", "Real Etarismo"],
                       columns=["Previsto Sem Etarismo", "Previsto Etarismo"])
print("\nMatriz de Confusão:")
print(conf_df)

# ETAPA 10: Importância das variáveis
importances = best_rf.feature_importances_
importance_df = pd.DataFrame({
    'Variável': X.columns,
    'Importância Média': importances
}).sort_values(by='Importância Média', ascending=False)
print("\nImportância das Variáveis:")
print(importance_df)

# ETAPA 11: Visualização de múltiplas árvores (Graphviz)
def visualizar_arvore(modelo, indice, nome_base="arvore_rf", max_depth=3):
    dot = export_graphviz(
        modelo.estimators_[indice],
        out_file=None,
        feature_names=X.columns,
        class_names=["Sem Etarismo", "Com Etarismo"],
        filled=True,
        rounded=True,
        special_characters=True,
        max_depth=max_depth
    )
    graph = graphviz.Source(dot)
    graph.render(f"{nome_base}_{indice}", format="png", cleanup=True)
    return graph

# Exibir as 3 primeiras árvores da floresta
N = 3
for i in range(N):
    print(f"\nVisualização da Árvore #{i}")
    arvore = visualizar_arvore(best_rf, i, max_depth=3)
    display(arvore)
