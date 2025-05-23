import streamlit as st

st.set_page_config(
    page_title="Master 2 Accounting Calculator",
    page_icon="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F014%2F919%2F451%2Foriginal%2Faccounting-analysis-3d-render-icon-png.png&f=1&nofb=1&ipt=e54e538b8f89fd3f52b547747cfa167f237423ff5c21e932eaa948e69c48ec12",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #848CCF;
        text-align: center;
        padding: 1.5rem 0;
        background: #0e1118;
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subject-header {
        color: #848CCF;
        font-size: 1.2rem;
        padding: 0.5rem 0;
        border-bottom: 2px solid #E2E8F0;
        margin-top: 1rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #848CCF;
        color: white;
    }
    .result-box {
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
        background-color: #0e1118;
        border: 1px solid #48BB78;
    }
    .semester-selector {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-bottom: 40px;
    }
    .semester-button {
        background-color: #4f8bf9;
        color: white;
        padding: 10px 30px;
        border-radius: 20px;
        text-align: center;
        cursor: pointer;
        width: 150px;
    }
    .semester-button.active {
        background-color: #2662de;
        font-weight: bold;
    }
    .s2-color {
        color: #848CCF;
    }
    /* Corner GIF Styles */
    .corner-gif {
        position: fixed;
        top: 100px;
        right: 10px;
        z-index: 9999;
        width: 80px;
        height: 80px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.8;
        transition: opacity 0.3s ease;
    }
    .corner-gif:hover {
        opacity: 1;
        transform: scale(1.1);
        transition: all 0.3s ease;
    }
    
    /* Alternative: Bottom right corner */
    .corner-gif-bottom {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.7;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <img src="https://media3.giphy.com/media/njON3jEmTYHEfRbfsk/200w.gif?cid=6c09b95286r0q4sdyv82fj0t6vx4gmmec7lipefp8jihytoe&ep=v1_stickers_search&rid=200w.gif&ct=s" class="corner-gif" alt="Finance GIF">
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-title">
        Master Accounting<br>Grade Calculator<br>
        <span style="font-size: 1.2rem; color: #dcdcdc;">By Sofiane Belkacem Nacer</span>
    </div>
    """, unsafe_allow_html=True)

# Define subjects and coefficients for each semester
s1_subjects = {
    "Marche Des Capitaux": 3,
    "Comptabilite Approfondie": 3,
    "Management Des Couts": 3,
    "Control De Gestion": 3,
    "Technique Bancaire": 3,
    "PMO": 3,
    "Planification Financiere": 3,
    "Strategie D'entreprise": 3,
    "Systeme d'Information de Gestion": 3,
    "Droit": 1.5,
    "Finance Publique": 1.5
}

s2_subjects = {
    "Droit pénal des affaires": 3,
    "ACSI": 3,
    "Audit comptable et financier": 3,
    "Économie managériale": 3,
    "Animation et contrôle budgétaire": 3,
    "Comptabilité des sociétés": 3,
    "Comptabilité publique 1": 3,
    "Stage": 3,
    "Méthodologie": 1.5,
    "Finance d'entreprise approfondie": 3,
    "Comptabilité des instruments financiers": 1.5
}

# Initialize session state for all subjects across all semesters
for subject in s1_subjects:
    exam_key = f"S1_{subject}_exam"
    td_key = f"S1_{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

for subject in s2_subjects:
    exam_key = f"S2_{subject}_exam"
    td_key = f"S2_{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

def calculate_semester_average(semester, subjects_with_coef):
    subjects_data = {}
    prefix = f"S{semester}_"
    
    for subject, coef in subjects_with_coef.items():
        exam_key = f"{prefix}{subject}_exam"
        td_key = f"{prefix}{subject}_TD"
        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade, "coef": coef}
        except (ValueError, TypeError):
            st.error(f"Entrée invalide pour {subject}. Veuillez saisir uniquement des nombres.")
            return

    total_weighted_sum = 0
    total_credits = sum(subjects_with_coef.values())
    
    for subject, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]

    semester_average = total_weighted_sum / total_credits
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total_weighted_sum)
    
    # Determine color based on average score
    color = "#FF0000"  # Default red for below 10
    if semester_average >= 15:
        color = "#D89CF6"  # Purple for 15 and up
    elif semester_average >= 14:
        color = "#12CAD6"  # Teal for 14-15
    elif semester_average >= 12:
        color = "#50D890"  # Green for 12-14
    elif semester_average >= 10:
        color = "#FE9801"  # Orange for 10-12
    
    st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2F855A; margin: 0;">📊 Résultats</h3>
            <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                Moyenne S{semester}: <strong style="color: {color}">{formatted_float}</strong><br>
                Total: <strong>{better_total}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

# Create tabs for semester selection
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    semester_tabs = st.tabs(["Semestre 1", "Semestre 2"])

# Display subjects and input fields based on selected semester
with semester_tabs[0]:
    st.markdown("<h2 style='text-align: center;'>Semestre 1</h2>", unsafe_allow_html=True)

    subjects_list = list(s1_subjects.keys())
    for subject in subjects_list:
        coef = s1_subjects[subject]
        st.markdown(f'<div class="subject-header">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)

        col_exam, col_td = st.columns(2)
        with col_exam:
            st.number_input(
                "Exam",
                key=f"S1_{subject}_exam",
                min_value=0.0,
                value=None,
                step=0.05,
                format="%.2f"
            )
        with col_td:
            st.number_input(
                "TD",
                key=f"S1_{subject}_TD",
                min_value=0.0,
                value=None,
                step=0.05,
                format="%.2f"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Calculer la Moyenne S1"):
            calculate_semester_average(1, s1_subjects)

with semester_tabs[1]:
    st.markdown("<h2 style='text-align: center;' class='s2-color'>Semestre 2</h2>", unsafe_allow_html=True)

    subjects_list = list(s2_subjects.keys())
    for subject in subjects_list:
        coef = s2_subjects[subject]
        st.markdown(f'<div class="subject-header s2-color">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)

        col_exam, col_td = st.columns(2)
        with col_exam:
            st.number_input(
                "Exam",
                key=f"S2_{subject}_exam",
                min_value=0.0,
                value=None,
                step=0.05,
                format="%.2f"
            )
        with col_td:
            st.number_input(
                "TD",
                key=f"S2_{subject}_TD",
                min_value=0.0,
                value=None,
                step=0.05,
                format="%.2f"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Calculer la Moyenne S2"):
        calculate_semester_average(2, s2_subjects)

# Add footer with credits
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
    <p style="color: #dcdcdc; margin: 0;">© 2025 Master 2 Accounting Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
