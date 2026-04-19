import streamlit as st
import math
from PIL import Image
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io
from datetime import datetime

# 1. ПЕРША КОМАНДА STREAMLIT
st.set_page_config(page_title="KnitFormula", layout="wide")

# 2. Функція для CSS
def local_css(file_name):
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    if os.path.exists(full_path):
        with open(full_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 3. Завантаження стилів
local_css("style.css")

# 4. Ініціалізація стану сторінок (ВИПРАВЛЕНО)
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Функції навігації
def go_to_offer(): st.session_state.page = 'offer'
def go_to_calc(): st.session_state.page = 'calc'
def go_to_welcome(): st.session_state.page = 'welcome'

# 5. Соцмережі
s1, s2, s3 = st.columns([1, 1, 1])
with s1: st.markdown('<div style="text-align:right"><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="22"></a></div>', unsafe_allow_html=True)
with s2: st.markdown('<div style="text-align:center"><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" width="22"></a></div>', unsafe_allow_html=True)
with s3: st.markdown('<div style="text-align:left"><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968804.png" width="22"></a></div>', unsafe_allow_html=True)

# --- 1. ВІТАЛЬНА СТОРІНКА (Ваш оригінальний текст) ---
if st.session_state.page == 'welcome':
    col_left, col_mid, col_right = st.columns([1.5, 4, 1.5])
    with col_mid:
        st.title("🧶 KnitFormula")
        st.markdown("""
        ### Привіт у KnitFormula! 👋

        Більше ніяких перев’язів та складних підрахунків на папері!
        Наш калькулятор **«Шапки: Модуль 1»** створений для того, щоб ви насолоджувалися в’язанням, поки ми рахуємо за вас.
        Ви отримаєте покроковий орієнтир і зрозумієте саму механіку створення ідеальної шапки.

        Нехай ваше в’язання буде легким, а результат — саме таким, як ви задумали. Додайте дрібку магії у кожен рядок! ✨
        """)
        st.button("ДАЛІ", on_click=go_to_offer)

    folder_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(folder_path):
        files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        with col_left:
            for filename in files[:4]:
                try:
                    img = Image.open(os.path.join(folder_path, filename))
                    st.image(img, use_column_width=True)
                except: st.write("🖼️")
        with col_right:
            for filename in files[4:8]:
                try:
                    img = Image.open(os.path.join(folder_path, filename))
                    st.image(img, use_column_width=True)
                except: st.write("🖼️")

# --- 2. ОФЕРТА (Ваш оригінальний текст) ---
elif st.session_state.page == 'offer':
    st.info("Будь ласка, ознайомтеся з умовами надання послуг перед початком використання.")
    st.markdown("""
    ДОГОВІР ПУБЛІЧНОЇ ОФЕРТИ<br>
    на придбання цифрового продукту під торговою маркою Knitformula<br>
    Цей Договір є офіційною та публічною пропозицією ФОП Раздобудко Наталії Миколаївни, яка діє під зареєстрованою торговою маркою Knitformula (далі – Продавець), укласти договір купівлі-продажу цифрового продукту на викладених нижче умовах.
    1. Предмет договору<br>
    1.1. Продавець зобов’язується передати Покупцеві цифровий продукт:<br>
    пряме посилання на веб-застосунок «Шапки Модуль 1» (авторська розробка ТМ Knitformula);<br>
    Смарт-опис однієї моделі, розроблений для використання з калькулятором;<br>
    Відео основних операцій, що стосуються моделі зі смарт-опису.<br>
    1.2. Передача продукту здійснюється в електронному вигляді шляхом надсилання посилання  або надання доступу після отримання повної оплати.<br>
    2. Порядок укладення договору<br>
    2.1. Акцептом (прийняттям) цієї оферти є 100% передоплата вартості продукту на банківський рахунок ФОП Продавця. <br>                                                                                                                                2.2. Оплата здійснюється за реквізитами, наданими Продавцем у приватному повідомленні (дірект), месенджерах або іншим погодженим способом.<br>             2.3. Після отримання оплати Продавець передає Покупцеві продукт протягом 1-2 робочих днів.<br>
    3. Права інтелектуальної власності<br>
    3.1. Усі складові цифрового продукту (веб-застосунок, тексти, відеоматеріали) є об’єктами авторського права та інтелектуальною власністю ТМ Knitformula.<br> 3.2. Покупець отримує обмежене право використовувати продукт виключно для особистих (некомерційних) потреб.<br>
    4. Права та обов’язки сторін<br>
    4.1. Покупець має право:<br>
    Отримати продукт у повному обсязі згідно з умовами цього договору.<br>
    4.2. Покупцю забороняється:<br>
    Передавати, продавати, копіювати, дарувати або поширювати продукт (чи будь-які його частини) третім особам;<br>
    Використовувати бренд, логотип або назву Knitformula для просування власних комерційних послуг без письмової згоди Продавця.<br>
    4.3. Продавець має право:<br>
    Отримати оплату в розмірі 100% вартості продукту;<br>
    В односторонньому порядку вносити зміни до тексту цієї Оферти.<br>
    5. Повернення коштів<br>
    5.1. Оскільки продукт має цифровий формат і доступ до нього надається Покупцеві одразу після оплати, що унеможливлює повернення товару, повернення грошових коштів не передбачено.<br>
    6. Відповідальність та штрафні санкції<br>
    6.1. Продавець не несе відповідальності за неможливість використання продукту через технічні особливості пристроїв чи програмного забезпечення Покупця.<br> 6.2. У разі виявлення факту розповсюдження Покупцем цифрового продукту ТМ Knitformula (платно або безоплатно) третім особам, Покупець зобов’язується виплатити Продавцю компенсацію у розмірі 100 000,00 грн за кожен випадок порушення авторських прав.<br>
    7. Інші умови<br>
    7.1. Укладення цього договору (оплата продукту) означає, що Покупець ознайомився з умовами використання авторських матеріалів ТМ Knitformula та беззастережно їх прийняв.<br>

    📌 Реквізити Продавця ФОП Раздобудко Наталія Миколаївна (ТМ Knitformula) Адреса: м. Запоріжжя, вул. Автозаводська, 48А\9<br>
     Р/р: UA233133990000026003055711775 в ПВ Запорізького РУ «Приватбанку» м. Запоріжжя<br> МФО: 313399 | ЄДРПОУ: 2541109245<br> Тел.: +38 (067) 595-01-35
    """, unsafe_allow_html=True)

    agree = st.checkbox("Я прочитав(ла) та погоджуюсь з умовами оферти")
    col_back, col_next = st.columns(2)
    with col_back:
        st.button("⬅ НАЗАД", on_click=go_to_welcome)
    with col_next:
        if st.button("ПРИЙНЯТИ ТА ПРОДОВЖИТИ"):
            if agree:
                st.session_state.page = 'calc'
                st.rerun()
            else:
                st.warning("Необхідно підтвердити згоду!")

# --- 3. КАЛЬКУЛЯТОР ---
elif st.session_state.page == 'calc':
    st.title("📏 Розрахунок моделі")
    container = st.container()
    with container:
        c1, c2 = st.columns(2)
        yarn_name = c1.text_input("Назва пряжі:", "Merino Gold")
        yarn_meters = c2.text_input("Метраж (м/у 100 г):", "125м/100г")
        hat_type = st.radio("Модель шапки:", ["Гарбузик", "Біні"])
        st.divider()

        col_left, col_right = st.columns(2)
        with col_left:
            head_circ = st.number_input("Обхват голови (см):", 40.0, 65.0, 54.0, 0.5)
            brim_h = st.number_input("Висота підвороту (см):", 0.0, 15.0, 0.0, 0.5)
            if hat_type == "Біні":
                num_wedges = st.selectbox("Кількість клинів:", [4, 5, 6, 8])
                crown_h = st.number_input("Висота маківки (см):", 3.0, 30.0, 5.0, 0.5)

            koef_map = {
                "шапка по голові (коротша, щільно по формі)": 0.40,
                "стандартна глибина (універсальна посадка)": 0.45,
                "глибока шапка з високою маківкою": 0.50
            }
            selected_text = st.selectbox("Коефіцієнт глибини:", list(koef_map.keys()))
            koef_glibini = koef_map[selected_text]

            visota_rezim = st.selectbox("Режим розрахунку висоти шапки:", ["Авто", "Вручну"])
            vlasna_visota = 0.0
            if visota_rezim == "Вручну":
                vlasna_visota = st.number_input("Введіть висоту шапки (см):", 10.0, 50.0, 20.0, 0.5)

        with col_right:
            if hat_type == "Біні":
                label_fabric = "Вид полотна:"
                fabric_options = ["гладь", "резинка 1*1", "резинка 2*2", "резинка 3*3"]
            else:
                label_fabric = "Вид резинки:"
                fabric_options = ["1*1", "2*2", "3*3"]
            rib_type = st.selectbox(label_fabric, fabric_options)
            dens_h = st.number_input("Щільність по горизонталі (п/см):", min_value=0.5, value=2.20, format="%.2f")
            dens_v = st.number_input("Щільність по вертикалі (р/см):", min_value=0.5, value=3.20, format="%.2f")
            dens_kar = st.number_input("Щільність на каретці/№ спиць:", min_value=0.0, value=1.00, format="%.2f")

        submit = st.button("РОЗРАХУВАТИ ✨", type="primary")

    if submit:
        # (Ваші оригінальні формули)
        if hat_type == "Біні":
            raw_loops = (head_circ * dens_h * 0.9)
            total_loops = round(raw_loops / num_wedges) * num_wedges
            wedge_width = total_loops // num_wedges
        else:
            step = {"1*1": 2, "2*2": 4, "3*3": 6}[rib_type]
            total_loops = round((head_circ * dens_h * 0.9) / step) * step

        h_val = vlasna_visota if visota_rezim == "Вручну" else (head_circ * koef_glibini)
        brim_rows = int(brim_h * dens_v)

        if hat_type == "Біні":
            reductions_per_wedge = wedge_width / 2
            reduction_rows_count = reductions_per_wedge / 2
            crown_rows_total = crown_h * dens_v
            reduction_step = crown_rows_total / reduction_rows_count if reduction_rows_count > 0 else 0
            rows_before_crown = int((h_val + brim_h - crown_h) * dens_v)
            total_rows = rows_before_crown + int(crown_rows_total)
        else:
            total_rows = int(h_val * dens_v) + int(brim_h * dens_v)
            rows_before_crown = total_rows

        results = {
            'total_loops': total_loops, 'total_rows': total_rows, 'brim_rows': brim_rows,
            'hat_type': hat_type, 'yarn_name': yarn_name, 'yarn_meters': yarn_meters,
            'head_circ': head_circ, 'rib_type': rib_type, 'dens_kar': dens_kar,
            'loops_1': int(total_loops/2), 'loops_2': int(total_loops/4)
        }
        if hat_type == "Біні":
            results.update({
                'num_wedges': num_wedges, 'wedge_width': wedge_width,
                'reduction_step': round(reduction_step, 1), 'rows_before_crown': rows_before_crown,
                'crown_h': crown_h, 'reduction_rows_count': int(reduction_rows_count)
            })

        st.session_state.results = results
        st.session_state.page = 'smart'
        st.rerun()


        # --- РЕЗУЛЬТАТИ ТА СМАРТ-ОПИС ---
elif st.session_state.page == 'smart':
    if 'results' not in st.session_state:
                st.warning("Будь ласка, спочатку виконайте розрахунок.")
                st.button("⬅ ДО КАЛЬКУЛЯТОРА", on_click=go_to_calc)
    else:
                res = st.session_state.results

                # 1. НАЛАШТУВАННЯ ШРИФТІВ ТА ФІГУРИ
                plt.rcParams["font.family"] = "serif"
                plt.rcParams["font.serif"] = ["Times New Roman"]

                fig = plt.figure(figsize=(10, 14))
                fig.patch.set_facecolor('white')

                if res['hat_type'] == "Біні":
                    report_title = "ПАРАМЕТРИ МОДЕЛІ"
                    params_text = (f"Виріб: шапка {res['hat_type']}\n"
                                   f"Пряжа: {res['yarn_name']} ({res['yarn_meters']})\n"
                                   f"Обхват голови: {res['head_circ']} см\n"
                                   f"Полотно/Резинка: {res['rib_type']}")

                    smart_text = (
                        f"1. Наберіть {res['total_loops']} петлі/петель на щільності/№ спиць {res['dens_kar']}.\n"
                        f"2. Пров'яжіть {res['rows_before_crown']-1} ряди/рядів (включаючи підворот) до початку клинів.\n"
                        f"3. У наступному ряду поділіть полотно на {res['num_wedges']} клинів по {res['wedge_width']} петель/петлі.\n"
                        f"4. Виконайте фасонні убавки в кожному клині з обох боків у кожному {round(res['reduction_step'])} ряду {res['reduction_rows_count']} раз.\n"
                        f"5. У міжубавочних рядах в'яжіть прямо зберігаючи візерунок.\n"
                        f"6. Зніміть усі петлі на голку та протягніть робочу нитку через них, щільно стягнувши маківку.\n"
                        f"7. Зшийте шапку матрацним швом."
                    )

                    plt.figtext(0.5, 0.96, report_title, fontsize=16, weight='bold', color='#8E7CC3', ha='center')
                    plt.figtext(0.05, 0.92, " ", fontsize=12, weight='bold')
                    plt.figtext(0.05, 0.915, params_text, fontsize=11, va='top', linespacing=1.5,
                                bbox=dict(boxstyle='round,pad=0.8', facecolor='#f9f9f9', edgecolor='#ddd'))

                    plt.figtext(0.05, 0.84, "СМАРТ-ОПИС:", fontsize=12, weight='bold')
                    plt.figtext(0.05, 0.835, smart_text, fontsize=11, va='top', linespacing=1.8)
                    plt.figtext(0.05, 0.58, "ТЕХНІЧНИЙ МАЛЮНОК:", fontsize=12, weight='bold')

                    ax = fig.add_axes([0.15, 0.2, 0.7, 0.35])
                    n = res['num_wedges']; width = 10; base_y = 5; wedge_w = width / n; crown_top_y = 12
                    ax.plot([0, width], [0, 0], color='black', lw=2)
                    ax.plot([0, 0], [0, base_y], color='black', lw=2)
                    ax.plot([width, width], [0, base_y], color='black', lw=2)

                    for i in range(n):
                        x_start = i * wedge_w; x_mid = x_start + (wedge_w / 2); x_end = (i + 1) * wedge_w
                        ax.plot([x_start, x_mid], [base_y, crown_top_y], color='black', lw=2)
                        ax.plot([x_mid, x_end], [crown_top_y, base_y], color='black', lw=2)
                        ax.text(x_mid, base_y - 0.7, f"{res['wedge_width']}", ha='center', fontsize=10)

                    num_steps = int(res['wedge_width'] / 4)
                    step_y = (crown_top_y - base_y) / num_steps if num_steps > 0 else 0
                    curr_row = res['rows_before_crown']
                    for j in range(num_steps + 1):
                        y_p = base_y + (j * step_y)
                        ax.plot([0, width], [y_p, y_p], color='green', ls='--', lw=0.5, alpha=0.6)
                        ax.text(-0.2, y_p, f"{int(curr_row)} р.", ha='right', va='center', fontsize=8)
                        curr_row += res['reduction_step']

                    if res['brim_rows'] > 0:
                        ax.plot([0, width], [2, 2], color='green', ls='--', lw=1)
                        ax.text(width + 0.2, 2, f"{res['brim_rows']} р. підгибу", fontsize=9, color='green')

                    ax.text(width/2, -1.2, f"{res['total_loops']} п.", ha='center', weight='bold', fontsize=12)
                    ax.set_xlim(-2, 13); ax.set_ylim(-2, 14); ax.axis('off')

                else:
                    # --- ПОВЕРНЕНА ЛОГІКА ГАРБУЗИКА ---
                    report_title = "ПАРАМЕТРИ МОДЕЛІ"
                    params_text = (f"Виріб: шапка {res['hat_type']}\n"
                                   f"Пряжа: {res['yarn_name']} ({res['yarn_meters']})\n"
                                   f"Обхват голови: {res['head_circ']} см\n"
                                   f"Полотно/Резинка: {res['rib_type']}")
                    smart_text = (
                        f"1. Наберіть {res['total_loops']} петель/петлі на щільності/№ спиць/гачка {res['dens_kar']}.\n"
                        f"2. Пров'яжіть {res['total_rows']-1} ряди/рядів резинкою {res['rib_type']} до убавок.\n"
                        f"3. Перша убавка у {res['total_rows']} ряду: кожна друга петля (залишиться {res['loops_1']} петель).\n"
                        f"4. Пров'яжіть 2 ряди.\n"
                        f"5. Перенесіть петлі на задню фонтуру (якщо в'яжете на машині).\n"
                        f"6. Друга убавка у {res['total_rows']+3} ряду: кожна друга петля (залишиться {res['loops_2']} петель).\n"
                        f"7. Пров'яжіть 2 ряди.\n"
                        f"8. Зніміть усі петлі на голку та протягніть робочу нитку через них, щільно стягнувши маківку.\n"
                        f"9. Зшийте шапку матрацним швом."
                    )

                    plt.figtext(0.5, 0.96, report_title, fontsize=16, weight='bold', color='#8E7CC3', ha='center')
                    plt.figtext(0.05, 0.915, params_text, fontsize=11, va='top', linespacing=1.5,
                                bbox=dict(boxstyle='round,pad=0.8', facecolor='#f9f9f9', edgecolor='#ddd'))
                    plt.figtext(0.05, 0.84, "СМАРТ-ОПИС:", fontsize=12, weight='bold')
                    plt.figtext(0.05, 0.835, smart_text, fontsize=11, va='top', linespacing=1.8)
                    plt.figtext(0.05, 0.58, "ТЕХНІЧНИЙ МАЛЮНОК:", fontsize=12, weight='bold')

                    ax = fig.add_axes([0.15, 0.2, 0.7, 0.35])
                    # Малювання контуру гарбузика
                    ax.plot([0, 10], [0, 0], color='black', lw=2)
                    ax.plot([0, 0], [0, 8], color='black', lw=2)
                    ax.plot([10, 10], [0, 8], color='black', lw=2)

                    import matplotlib.patches as patches
                    arc = patches.Arc((5, 8), 10, 6, theta1=0, theta2=180, lw=2, color='black')
                    ax.add_patch(arc)

                    # Показники для гарбузика (Повернення з первинного)
                    if res['brim_rows'] > 0:
                        ax.plot([0, 10], [2, 2], color='green', ls='--', lw=1)
                        ax.text(10.2, 2, f"{res['brim_rows']} р. підгибу", fontsize=9, color='green')

                        # --- ПЕРША УБАВКА ---
                        ax.plot([0, 10], [8, 8], color='green', ls='--', lw=1)
                        ax.text(10.2, 8, f"{res['total_rows']} р.", fontsize=9, va='center')
                        ax.text(5, 8.2, f"{res['loops_1']} п.", ha='center', fontsize=10)

                # --- ДРУГА УБАВКА (ПОВЕРНУТО) ---
                        ax.plot([1.5, 8.5], [10, 10], color='green', ls='--', lw=1)
                        ax.text(8.7, 10, f"{res['total_rows']+3} р.", fontsize=9, va='center')
                        ax.text(5, 10.2, f"{res['loops_2']} п.", ha='center', fontsize=10)

                # Додаткові елементи
                        if res['brim_rows'] > 0:
                            ax.plot([0, 10], [2, 2], color='green', ls='--', lw=1)
                            ax.text(10.2, 2, f"{res['brim_rows']} р. підгибу", fontsize=9, color='green')

        # Загальна кількість петель знизу
                            ax.text(5, -0.8, f"{res['total_loops']} п.", ha='center', weight='bold', fontsize=12)

                            ax.set_xlim(-1, 14); ax.set_ylim(-2, 12); ax.axis('off')

                # --- ВІДОБРАЖЕННЯ ТА ВІДЕО ---
                st.pyplot(fig)

                st.markdown("---")
                st.markdown("### Відеоінструкції")
                v_col1, v_col2, v_col3 = st.columns(3)
                if res['hat_type'] == "Біні":
                    with v_col1: st.video("https://youtu.be/9TDPhgEQjTY")
                    with v_col2: st.video("https://youtu.be/YtQilrx9PlA")
                    with v_col3: st.video("https://youtu.be/Bru0SbCVptM")
                else:
                    with v_col1: st.video("https://youtu.be/9TDPhgEQjTY")
                    with v_col2: st.video("https://youtu.be/HgsN__pF7fA")
                    with v_col3: st.video("https://youtu.be/eWvXlDmyNyQ")

                # --- КНОПКИ ---
                st.markdown("<br>", unsafe_allow_html=True)
                # --- СТИЛІЗАЦІЯ КНОПОК (додайте це перед колонками кнопок) ---
                st.markdown("""
                            <style>
                                /* Стилізуємо всі кнопки, включаючи download_button */
                                div.stButton > button, div.stDownloadButton > button {
                                    background-color: #8E7CC3 !important; /* Ваш фіолетовий колір */
                                    color: white !important;
                                    border-radius: 5px;
                                    border: none;
                                    height: 3em;
                                    width: 100%;
                                }
                                /* Ефект при наведенні */
                                div.stButton > button:hover, div.stDownloadButton > button:hover {
                                    background-color: #7665A5 !important;
                                    color: white !important;
                                }
                            </style>
                        """, unsafe_allow_html=True)


                col_1, col_2, col_3 = st.columns(3)

                with col_1:
                    st.button("⬅ НАЗАД ДО РОЗРАХУНКУ", on_click=go_to_calc, use_container_width=True)

                with col_2:
            # Генеруємо буфер для завантаження
                    buf = io.BytesIO()
                    fig.savefig(buf, format="png", bbox_inches='tight', dpi=200)

            # Стандартна кнопка завантаження (вона автоматично підтягне стиль теми)
                    st.download_button(
                label="💾 ЗБЕРЕГТИ",
                data=buf.getvalue(),
                file_name=f"KnitFormula_{res['hat_type']}.png",
                mime="image/png",
                use_container_width=True
            )

                with col_3:

                    if st.button("🚪 НА ГОЛОВНУ", use_container_width=True):
                # Повністю очищаємо сесію
                        st.session_state.clear()
                        st.rerun()
