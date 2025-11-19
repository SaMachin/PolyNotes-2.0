"""
Construction des graphiques pour l'application
"""

import matplotlib.pyplot as plt
import numpy as np
from data import dataFramify

df_normalized, _ = dataFramify()

#fig1------------------------------

df_normalized["Type"] = df_normalized["Cours"].str.extract(r"^([A-Z]+)")

avg_by_type = df_normalized.groupby("Type")["Moyenne du groupe"].mean().sort_values()
fig1, ax = plt.subplots()
ax.bar(avg_by_type.index, avg_by_type.values)
ax.set_xlabel("Type de cours (sigle)")
ax.set_ylabel("Note moyenne")
ax.set_title("Note moyenne par type de sigle")
ax.set_ylim(0, 4)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.set_xticklabels(avg_by_type.index, rotation=45, ha='right')

#fig2------------------------------

# Extraire année et trimestre
df_normalized["Annee"] = df_normalized["Session"].str.extract(r"(\d+)").astype(int)
df_normalized["Trimestre"] = df_normalized["Session"].str.extract(r"([AHEÉ])")[0].replace({"É": "E"})

# Calcul moyenne par année + trimestre
avg_by_year_trim = df_normalized.groupby(["Annee", "Trimestre"])["Moyenne du groupe"].mean().unstack(fill_value=0)
trimestres = ["A", "H", "E"]
colors = {"A":"#4CAF50", "H":"#2196F3", "E":"#FF9800"}

# Moyenne totale par année (pour la ligne superposée)
avg_by_year_total = df_normalized.groupby("Annee")["Moyenne du groupe"].mean().sort_index()

# Graphique multi-barres + ligne moyenne globale
fig2, ax = plt.subplots(figsize=(8,5))
x = np.arange(len(avg_by_year_trim.index))
width = 0.25

# Barres par trimestre
for i, trimestre in enumerate(trimestres):
    if trimestre in avg_by_year_trim.columns:
        ax.bar(x + i*width, avg_by_year_trim[trimestre], width, label=trimestre, color=colors[trimestre])

# Ligne moyenne globale par année
ax.plot(x + width, avg_by_year_total.values, color='black', marker='o', linestyle='-', linewidth=2, label='Moyenne annuelle')


ax.set_xlabel("Année")
ax.set_ylabel("Note moyenne")
ax.set_title("Moyenne des notes par année et par trimestre avec moyenne globale")
ax.set_xticks(x + width)
ax.set_xticklabels(avg_by_year_trim.index)
ax.set_ylim(0, 4)
ax.legend(title="Trimestre", loc='lower left')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajouter valeurs au-dessus des barres
for i, annee in enumerate(avg_by_year_trim.index):
    for j, trimestre in enumerate(trimestres):
        if trimestre in avg_by_year_trim.columns:
            v = avg_by_year_trim.loc[annee, trimestre]
            ax.text(i + j*width, v + 0.05, f"{v:.2f}", ha='center', fontsize=8)
    # Valeur ligne moyenne globale
    v_total = avg_by_year_total.loc[annee]
    ax.text(i + width, v_total + 0.05, f"{v_total:.2f}", ha='center', fontsize=9, fontweight='bold', color='black')

plt.tight_layout()