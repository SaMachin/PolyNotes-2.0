"""
Repertoire des fonctions utilitaires
"""

def note_to_letter(note):
    """Convertit une note numérique en lettre selon le barème."""
    note = float(note)
    if note >= 4.0:
        return "A"
    elif note >= 3.5:
        return "B+"
    elif note >= 3.0:
        return "B"
    elif note >= 2.5:
        return "C+"
    elif note >= 2.0:
        return "C"
    elif note >= 1.5:
        return "D+"
    elif note >= 1.0:
        return "D"
    else:
        return "F"

def color_letters(val):
    """Applique une couleur aux lettres de note pour l'affichage."""
    color_map = {
        "A": "green",
        "B+": "blue",
        "B": "blue",
        "C+": "yellow",
        "C": "yellow",
        "D+": "orange",
        "D": "orange",
        "F": "red"
    }
    
    return f"color: {color_map.get(val, 'black')}"

def session_sort_key(session):
    """
    Génère une clé de tri pour les sessions.
    Ex: A2021 < H2021 < E2021 < A2022 ...
    """
    session = session.strip().upper().replace("É", "E")

    if len(session) < 2:
        return (999, 999)

    letter = session[0]
    num = int(session[1:]) if session[1:].isdigit() else 999

    order_map = {"A": 1, "H": 2, "E": 3}

    return (num, order_map.get(letter, 999))

def check_data_quality(df):
    """Vérifie s'il y a des anomalies dans les données"""
    issues = []

    if df["Moyenne du groupe"].isnull().any():
        issues.append("⚠️ Certaines notes sont manquantes.")

    if df["Session"].isnull().any():
        issues.append("⚠️ Certaines sessions sont vides.")
    invalid_sessions = df[~df["Session"].str.match(r"^[AHEÉ]\d+$", na=False)]

    if not invalid_sessions.empty:
        issues.append(f"⚠️ {len(invalid_sessions)} sessions invalides détectées.")

    over_max = df[df["Moyenne du groupe"] > 4.0]
    if not over_max.empty:
        issues.append(f"❗ {len(over_max)} note(s) > 4.0 détectée(s).")

    if len(issues) == 0:
        issues.append("✅ Aucune anomalie détectée.")

    return issues