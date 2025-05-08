import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("State_of_data_BR_2023_Kaggle-df_survey_2023_maior_50 - Worksheet.csv")

df.columns = [col[1].strip() if isinstance(col, tuple) else col for col in df.columns]

# Alvo: experiência profissional afetada
target_col = "('P1_e ', 'experiencia_profissional_prejudicada')"
y_true_raw = df[target_col]
y_true = y_true_raw.dropna()
le = LabelEncoder()
y_true_encoded = le.fit_transform(y_true)

df_sim = df.loc[y_true.index]

col_train_video = [col for col in df.columns if "Imagens, Vídeos" in col]
col_satisf = [col for col in df.columns if "satisfação_profissional" in col]

def simple_tree_rule(row):
    train = any(row.get(col) == 1 for col in col_train_video)
    satisf = any(row.get(col) == 0 for col in col_satisf)  # insatisfação
    return 1 if train or satisf else 0

y_pred_simulated = df_sim.apply(simple_tree_rule, axis=1)

cm = confusion_matrix(y_true_encoded, y_pred_simulated)

remover_indices = [7, 4, 2, 1]
keep_indices = [i for i in range(len(le.classes_)) if i not in remover_indices]

cm_filtered = cm[np.ix_(keep_indices, keep_indices)]
short_labels_filtered = [f"P1_{i}" for i in keep_indices]

# Plotagem da matriz de confusão filtrada
plt.figure(figsize=(5.5, 4.5))
sns.heatmap(cm_filtered, annot=True, fmt="d", cmap="Blues",
            xticklabels=short_labels_filtered, yticklabels=short_labels_filtered)
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão Filtrada - Experiência Profissional Afetada")
plt.tight_layout()
plt.show()
