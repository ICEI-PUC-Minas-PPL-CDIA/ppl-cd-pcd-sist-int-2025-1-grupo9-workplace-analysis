import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
import graphviz

df = pd.read_csv("base_unificada_limpa.xlsx - Sheet1.csv")
features = [ 'gênero',
        'cor/raça/etnia',
        'faixa_etária',
        'pcd',
        'anos_de_experiência',
        'área_de_atuação',
        'nível_de_escolaridade',
        'salário',
        'tipo_de_empresa',
        'tamanho_da_empresa',
        'satisfação_profissional',
        'oportunidades_de_promoção',
        'adequação_às_novas_tecnologias',
        'incentivo_à_diversidade_etária_na_empresa',
        'planos_de_aposentadoria_e_transição_de_carreira',
        'flexibilidade_de_trabalho_para_profissionais_55+',
        'acesso_a_treinamentos_e_capacitações',
        'frequência_de_atualização_profissional'
       ]
target = 'sentimento_de_valorização_na_empresa'

df_model = df[features + [target]].dropna()
X_dict = df_model[features].T.to_dict().values()
vect = DictVectorizer(sparse=False)
X_train = vect.fit_transform(X_dict)

le = LabelEncoder()
y_train = le.fit_transform(df_model[target])

model = DecisionTreeClassifier(criterion='entropy', random_state=0)
model.fit(X_train, y_train)

# Exporta a árvore como DOT
dot_data = export_graphviz(
    model,
    out_file=None,
    feature_names=vect.feature_names_,
    class_names=le.classes_.astype(str),
    filled=True,
    rounded=True,
    special_characters=True
)

# Gera o gráfico
graph = graphviz.Source(dot_data)
graph.render("arvore_limpa_graphviz", format="png", cleanup=True
             arvore_limpa_graphviz.png
