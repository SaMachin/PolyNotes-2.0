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
* Assurer la **pérennité du projet** en faisant un projet open source
* Ajouter une **validation automatique des données**, ce qui permet de ne pas faire planter Google Sheets (probablement ce qui a tué le projet de u/PolyCrowdsourced 😅)

---

* Pour contribuer au registre de notes: [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeq0mzVsHSnFjtHvvJbmBOA2-SiFuXF2hggwZl3Ia99VuTaZw/viewform?usp=pp_url&entry.1761690987=COURS1+-+MOYENNE1%0ACOURS2+-+MOYENNE2%0ACOURS3+-+MOYENNE3)
* Pour aller explorer les données: [Google Sheets](https://docs.google.com/spreadsheets/d/1ILE5D97Ea0444sMdJCCgDsLRrD8aFfEBBIUMot9CaKM/edit?usp=sharing)

---

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://polynotes-2.streamlit.app/)

### Comment rouler le projet localment

1. Télécharger les dépendances

   ```
   $ pip install -r requirements.txt
   ```

2. Lancer l'app

   ```
   $ streamlit run src/app.py
   ```
3. Enjoy 🤙