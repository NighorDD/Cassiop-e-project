import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

subtypes_colors = {"LumP" : "green", "Ba/Sq" : "blue", "LumU" : "red", "Stroma-rich" : "yellow", "LumNS" : "pink", "NE-like" : "orange"}

Dataframe_labels = pd.read_csv("../../BLCA_DATA/labels_str.csv")
Dataframe_link = pd.read_csv("../../BLCA_DATA/CLINICAL/PROCESSED/patient_norm.csv")
Dataframe_node= pd.read_csv("../../BLCA_DATA/OMICS/PROCESSED/gene-expression_norm.csv")

node_colors = []

# Calcul de la similarité entre les patients
patient_similarity = cosine_similarity(Dataframe_link.iloc[:, 1:])

for i in range(len(patient_similarity)):
    for j in range(len(patient_similarity)):
        if (patient_similarity[i, j] < 0.5) or (i == j):
            patient_similarity[i, j] = 0

    node_colors.append(subtypes_colors[Dataframe_labels.iloc[i]['class']])

# Dessin du graphe avec les noeuds colorés selon la maladie
G = nx.from_numpy_array(patient_similarity)
nx.draw(G, with_labels=True)
plt.show()
