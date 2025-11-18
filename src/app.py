"""
Structure des pages de l'application
"""

import streamlit as st
from utils import *
from data import gen_data
st.title("PolyNotes 2.0")

tab1, tab2, tab3 = st.tabs(["📋 Données", "📈 Graphique des notes", "🗿 About"])

avg_df, df_normalized, error_logs = gen_data()

# ---------------------------
# Barre de recherche pour filtrer un cours
# ---------------------------
search_course = st.text_input("🔎 Rechercher un cours (sigle)").strip()
if search_course:
    filtered_df = avg_df[avg_df["Cours"].str.upper().str.contains(search_course.upper())]
else:
    filtered_df = avg_df

# ---------------------------
# Moyenne a travers toutes les sessions
# ---------------------------
if search_course:
        global_avg = df_normalized[df_normalized["Cours"].str.upper().str.contains(search_course.upper())]["Moyenne du groupe"].mean()
        st.markdown(f"**📌 Moyenne du cours '{search_course.upper()}' à travers toutes les sessions : {round(global_avg,2)} | {note_to_letter(global_avg)}**")

with tab1:
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("### Barème" \
        "")
        st.markdown("""
        🟢 **A** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [4, 4]   
        🔵 **B+, B**  &nbsp; [3, 4[  
        🟡 **C+, C**  &nbsp; [2, 3[  
        🟠 **D+, D**  &nbsp; [1, 2[   
        🔴 **F** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[0, 1[
        """)

    with col2:
        # ---------------------------
        # Affichage Streamlit avec couleurs
        # ---------------------------
        st.subheader("📊 Registre des moyennes")

        st.dataframe(filtered_df.style.applymap(color_letters, subset=["Lettre"]))

        # ---------------------------
        # Bouton Debugger
        # ---------------------------
        st.markdown("---")
        if st.toggle("DEBUG VIEW"):
            issues = check_data_quality(df_normalized)
            if len(error_logs) == 0:
                st.success("Aucune erreur détectée 🎉")
            else:
                for err in error_logs:
                    st.text(err)
            for issue in issues:
                if "✅" in issue:
                    st.success(issue)
                else:
                    st.warning(issue)

with tab2:
    from graph import fig1, fig2
    st.pyplot(fig1)
    st.pyplot(fig2)

    st.markdown("Faites ce que vous voulez de ces graphiques, je les ai faits pour le fun, mais ils ne servent à rien")

with tab3:
    st.markdown(
        """
        ## Infos sur PolyNotes 2.0

        PolyNotes 2.0 est un tableau de bord interactif pour explorer 
        les notes moyennes des cours de Polytechnique Montréal.

        Ce projet est inspiré du 
        [projet](https://docs.google.com/spreadsheets/d/1waI3NYgmy_oPJmx49hr5VjXat5jjmP6rcM8vHtzc73w/edit?gid=0#gid=0) 
        du très honorable **u/PolyCrowdsourced**. Il a pour but de prendre la relève de son projet pour 
        faire revivre un outil génial qui commençait à prendre la poussière.

        ---

        #### PolyNotes 2.0 vise à :
        * Offrir une interface plus ✨**jolie**✨ et plus interactive.
        * Assurer la **pérennité du projet** en faisant un projet [open source](https://github.com/SaMachin/PolyNotes-2.0/tree/main)
        * Ajouter une **validation automatique des données**, ce qui permet de ne pas faire planter Google Sheets (probablement ce qui a tué le projet de u/PolyCrowdsourced 😅)

        ---

        * Pour contribuer au registre de notes: [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeq0mzVsHSnFjtHvvJbmBOA2-SiFuXF2hggwZl3Ia99VuTaZw/viewform?usp=pp_url&entry.1761690987=COURS1+-+MOYENNE1%0ACOURS2+-+MOYENNE2%0ACOURS3+-+MOYENNE3)
        * Pour aller explorer les données: [Google Sheets](https://docs.google.com/spreadsheets/d/1ILE5D97Ea0444sMdJCCgDsLRrD8aFfEBBIUMot9CaKM/edit?usp=sharing)
        * Pour aller explorer les engrenages du projet : [Git Hub](https://github.com/SaMachin/PolyNotes-2.0/tree/main)
        """
    )