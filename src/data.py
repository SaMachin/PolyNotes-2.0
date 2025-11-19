"""
Traitement et normalisation des données
"""

import pandas as pd
from utils import *

sheet_id = "1ILE5D97Ea0444sMdJCCgDsLRrD8aFfEBBIUMot9CaKM"
gid = "1856131741"

csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"


def gen_data():
    df = pd.read_csv(csv_url, sep=",", encoding="utf-8")
    # ---------------------------
    # Normalisation des données
    # ---------------------------
    rows = []
    error_logs = []

    for _, row in df.iterrows():
        session = row["Sélection de la session"]
        horodatage = row["Horodatage"]
        for course_grade in str(row["Moyennes"]).split("\n"):
            text = course_grade.strip()
            if not text:
                continue

            if " - " not in text:
                text = text.replace(" ", "")
            try:
                sigle, grade = course_grade.split("-")
                grade = float(grade.replace(",", "."))
                rows.append({
                    "Horodatage": horodatage,
                    "Session": session,
                    "Cours": sigle.strip().upper(),
                    "Moyenne du groupe": grade
                })
            except Exception as e:
                error_logs.append(f"Erreur pour la ligne : '{course_grade}' → {e}")

    df_normalized = pd.DataFrame(rows)

    # ---------------------------
    # Calcul moyenne par cours & session
    # ---------------------------
    avg_df = df_normalized.groupby(["Cours", "Session"], as_index=False)["Moyenne du groupe"].mean()
    avg_df = avg_df.sort_values(by=["Cours", "Session"]).reset_index(drop=True)

    # ---------------------------
    # Format float 2 décimales + conversion lettre
    # ---------------------------
    avg_df["Moyenne du groupe"] = avg_df["Moyenne du groupe"].map(lambda x: f'{round(x, 2):.2f}')
    avg_df["Lettre"] = avg_df["Moyenne du groupe"].map(note_to_letter)

    # ---------------------------
    # Trie en fonction du sigle puis de la session
    # ---------------------------
    avg_df["SortKey"] = avg_df["Session"].map(session_sort_key)
    avg_df = avg_df.sort_values(by=["Cours", "SortKey"]).drop(columns="SortKey").reset_index(drop=True)
    
    return avg_df, df_normalized, error_logs