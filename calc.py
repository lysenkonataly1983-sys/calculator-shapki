import streamlit as st
import math

# 1. Налаштування сторінки
st.set_page_config(page_title="KnitFormula - Шапки: Модуль 1", page_icon="🧶")

# 2. Глобальні стилі
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tinos:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Tinos', serif !important; }

    #screenshot-area {
        padding: 30px;
        background: white;
        border: 1px solid #eee;
        border-radius: 15px;
        color: black !important;
        width: 600px;
        margin: auto;
    }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'calculated' not in st.session_state:
    st.session_state.calculated = False

# --- ВІТАЛЬНЕ ВІКНО ---
if st.session_state.page == 'welcome':
    try:
        st.image("image_06b417.jpg", width=250)
    except:
        st.subheader("TM KnitFormula")

    st.title("Привіт у KnitFormula! 👋")
    st.markdown("""
    Більше ніяких перев’язів та складних підрахунків на папері! <br>
    Наш калькулятор **«Шапки: Модуль 1»** створений для того, щоб ви насолоджувалися в’язанням, поки ми рахуємо за вас.
    """, unsafe_allow_html=True)

    with st.expander("Читати Договір публічної оферти", expanded=False):
        st.markdown("""
        **ДОГОВІР ПУБЛІЧНОЇ ОФЕРТИ**
        Цей Договір є офіційною пропозицією ФОП Раздобудко Наталії Миколаївни.
        1. **Власність**: Усі алгоритми та дизайн є інтелектуальною власністю автора.
        2. **Відповідальність**: Результати мають рекомендаційний характер.
        """)

    agree = st.checkbox("Я ознайомлений(а) з договором оферти та приймаю його умови", key="agree_final")
    if st.button("ПОЧАТИ РОЗРАХУНОК"):
        if agree:
            st.session_state.page = 'calc'
            st.rerun()
        else:
            st.error("Будь ласка, підтвердіть згоду з офертою.")

# --- ВІКНО КАЛЬКУЛЯТОРА ---
elif st.session_state.page == 'calc':
    st.title("🧶 Калькулятор «Шапки: Модуль 1»")

    with st.expander("📏 Введення даних", expanded=not st.session_state.calculated):
        col_y1, col_y2 = st.columns(2)
        with col_y1:
            yarn_name = st.text_input("Назва пряжі:", "Merino 100%")
        with col_y2:
            yarn_meters = st.text_input("Метраж (м/100г або м/50г):", "150м / 50г")

        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            hat_type = st.radio("Модель:", ["Гарбузик", "Біні"], horizontal=True)
            head_circ = st.number_input("Окружність голови (см):", min_value=45.0, value=54.0, step=0.5)
            brim_h_cm = st.number_input("Висота підвороту (см):", 0.0, step=0.5)
        with col2:
            rib_type = st.selectbox("Вид резинки:", ["1*1", "2*2", "3*3"])
            # ОНОВЛЕНО НАЗВИ ЩІЛЬНОСТІ
            dens_h = st.number_input("Щільність по горизонталі (петель в 1 см):", min_value=0.5, value=2.20, format="%.2f")
            dens_v = st.number_input("Щільність по вертикалі (рядів в 1 см):", min_value=0.5, value=3.20, format="%.2f")

    if st.button("ВЕРШИТИ МАГІЮ ✨"):
        st.session_state.calculated = True

    if st.session_state.calculated:
        step = {"1*1": 2, "2*2": 4, "3*3": 6}[rib_type]
        total_loops = math.floor((head_circ * dens_h * 0.9) / step) * step
        brim_rows = round(brim_h_cm * dens_v)
        total_rows = round(head_circ * 0.45 * dens_v) + brim_rows
        loops_1, loops_2 = int(total_loops / 2), int(total_loops / 4)

        svg_code = f"""
        <svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
            <path d="M 100,260 L 100,120 A 100,80 0 0 1 300,120 L 300,260 Z" fill="none" stroke="black" stroke-width="2.5" />
            <line x1="105" y1="120" x2="295" y2="120" stroke="green" stroke-dasharray="5,5" />
            <text x="185" y="115" font-family='Times New Roman' font-size="14" font-weight="bold" fill="black">{loops_1} п.</text>
            <text x="310" y="125" font-family='Times New Roman' font-size="14" fill="black" font-weight="bold">{total_rows} р.</text>
            <line x1="130" y1="80" x2="270" y2="80" stroke="green" stroke-dasharray="5,5" />
            <text x="185" y="75" font-family='Times New Roman' font-size="14" font-weight="bold" fill="black">{loops_2} п.</text>
            <text x="310" y="85" font-family='Times New Roman' font-size="14" fill="black" font-weight="bold">{total_rows + 2} р.</text>
            {"<line x1='100' y1='210' x2='300' y2='210' stroke='green' stroke-dasharray='5,5' />" if brim_rows > 0 else ""}
            {"<text x='310' y='215' font-family='Times New Roman' font-size='12' fill='black'>" + str(brim_rows) + " р. підгибу</text>" if brim_rows > 0 else ""}
            <text x="175" y="290" font-family='Times New Roman' font-size="16" font-weight="bold" fill="black">{int(total_loops)} п.</text>
        </svg>"""

        clean_desc = f"""1. Наберіть {int(total_loops)} петель.
2. Пров'яжіть {int(total_rows - 1)} рядів резинкою {rib_type}.
3. У {int(total_rows)} рядку виконайте убавки кожної другої петлі ({loops_1} п. залишається).
4. Пров'яжіть 2 ряди.
5. Перенесіть петлі на задню фонтуру.
6. Виконайте другу убавку кожної другої петлі ({loops_2} п. залишається).
7. Пров'яжіть 2 ряди.
8. Зніміть усі петлі та стягніть маківку.
9. Зшийте матрацним швом."""

        st.markdown(f"""
        <div id="screenshot-area">
            <h2 style="text-align:center; color:black; margin-top:0;">Технологічна карта KnitFormula</h2>
            <table style="width:100%; border: 1px solid black; border-collapse: collapse; margin-bottom: 15px; color:black; font-size:14px;">
                <tr><td style="border: 1px solid black; padding: 5px; font-weight:bold;">Пряжа / Метраж</td><td style="border: 1px solid black; padding: 5px;">{yarn_name} / {yarn_meters}</td></tr>
                <tr><td style="border: 1px solid black; padding: 5px; font-weight:bold;">Обхват голови</td><td style="border: 1px solid black; padding: 5px;">{head_circ} см</td></tr>
                <tr><td style="border: 1px solid black; padding: 5px; font-weight:bold;">Щільність (петель в 1 см та рядів в 1 см)</td><td style="border: 1px solid black; padding: 5px;">Г: {dens_h} петель в 1 см | В: {dens_v} рядів в 1 см</td></tr>
                <tr><td style="border: 1px solid black; padding: 5px; font-weight:bold;">Модель / Резинка</td><td style="border: 1px solid black; padding: 5px;">{hat_type} / {rib_type}</td></tr>
            </table>
            <div style="text-align:center;">{svg_code}</div>
            <h3 style="color:black; margin-top:10px;">Інструкція:</h3>
            <div style="font-size: 14px; color:black; white-space: pre-wrap; line-height: 1.4;">{clean_desc}</div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.components.v1.html(f"""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
            <button onclick="savePng()" style="width:100%; height:45px; background-color:#FF4B4B; color:white; border:none; border-radius:8px; cursor:pointer; font-family:'Tinos', serif; font-size:16px; font-weight:bold;">
                📸 ЗБЕРЕГТИ КАРТКУ (PNG)
            </button>
            <script>
            function savePng() {{
                const area = window.parent.document.getElementById('screenshot-area');
                html2canvas(area, {{ useCORS: true, scale: 2, backgroundColor: "#ffffff" }}).then(canvas => {{
                    const link = document.createElement('a');
                    link.download = 'KnitFormula_{hat_type}_{int(head_circ)}.png';
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                }});
            }}
            </script>
        """, height=60)

    if st.button("⬅ Назад"):
        st.session_state.page = 'welcome'
        st.session_state.calculated = False
        st.rerun()
