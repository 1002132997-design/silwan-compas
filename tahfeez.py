import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة مدرسة سلوان - نظام التقييم المعياري", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebarViewPort"], div, p, h1, h2, h3, input, label, .stTextArea {
        font-family: 'Cairo', sans-serif; direction: RTL; text-align: right;
    }
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #f8f9fa; color: #004d40;
        text-align: center; padding: 10px; font-weight: bold;
        border-top: 3px solid #009688; z-index: 100;
    }
    .main-title { color: #00695c; text-align: center; border-bottom: 2px solid #009688; padding-bottom: 10px; }
    .section-head { background-color: #f1f8e9; padding: 8px; border-right: 5px solid #2e7d32; border-radius: 5px; color: #1b5e20; font-weight: bold; margin: 15px 0 10px 0; }
    /* تنسيق أزرار نعم/لا لتكون بجانب النص */
    .stRadio > div { flex-direction: row !important; gap: 20px; }
    </style>
    <div class="footer">فكرة وتطوير: مها سرحان © 2024 | جميع الحقوق محفوظة لمدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

# --- الترويسة ---
logo_url = "https://i.ibb.co/Xz9N47h/silwan-logo.png"
st.image(logo_url, width=120)
st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان الابتدائية الجديدة</h1>", unsafe_allow_html=True)
st.write(f"**مدير المدرسة:** الأستاذ يحيى نابلسي | **مركزة التربية الخاصة:** مها سرحان")
st.markdown("---")

# === البيانات التعريفية ===
col1, col2, col3 = st.columns(3)
with col1:
    student_name = st.text_input("اسم الطالب:")
    student_id = st.text_input("رقم الهوية:")
with col2:
    student_class = st.text_input("الصف:")
    teacher_mrbia = st.text_input("اسم المربي/ة:")
with col3:
    matia_years = st.text_input("عدد السنوات في ماتيا:")
    report_date = st.date_input("تاريخ التقرير:", date.today())

# دالة مساعدة لإنشاء صفوف التقييم
def evaluation_row(label, key):
    col_text, col_choice = st.columns([3, 1])
    with col_text:
        st.write(label)
    with col_choice:
        choice = st.radio("", ["نعم", "لا", "جزئياً"], key=key, horizontal=True, label_visibility="collapsed")
    return label if choice == "نعم" else (f"{label} (بشكل جزئي)" if choice == "جزئياً" else None)

st.header("📋 استمارة التوصيف (نظام نعم/لا)")
tabs = st.tabs(["🏛️ السلوكي والاجتماعي", "📖 اللغة العربية", "🧮 الحساب", "🧠 النمائي والوظيفي"])

# --- الجانب السلوكي ---
with tabs[0]:
    st.markdown("<div class='section-head'>مهارات التعلم والسلوك الاجتماعي</div>", unsafe_allow_html=True)
    m_s_list = ["الانتظام بالوصول بالوقت المناسب", "المواظبة على إحضار الأدوات", "تحضير الواجبات البيتية", "الالتزام بالقوانين المدرسية", "بناء علاقات اجتماعية إيجابية", "فهم المواقف الاجتماعية"]
    sel_s = []
    for i, m in enumerate(m_s_list):
        res = evaluation_row(m, f"s_{i}")
        if res: sel_s.append(res)
    note_s = st.text_area("إضافات المربي (الجانب السلوكي):", placeholder="اكتب هنا أي ملاحظات إضافية...")

# --- اللغة العربية ---
with tabs[1]:
    st.markdown("<div class='section-head'>القراءة ومستويات الفهم</div>", unsafe_allow_html=True)
    m_r_list = ["تمييز الحروف والحركات", "القراءة بدقة وطلاقة", "تحديد تفاصيل (مستوى حرفي)", "استنتاج نتائج (مستوى تفسيري)", "اقتراح حلول (مستوى تطبيقي)"]
    sel_r = []
    for i, m in enumerate(m_r_list):
        res = evaluation_row(m, f"r_{i}")
        if res: sel_r.append(res)
    
    st.markdown("<div class='section-head'>الكتابة والتعبير</div>", unsafe_allow_html=True)
    m_w_list = ["الخط مقروء ومرتب", "إملاء صحيح", "صياغة أفكار منظمة"]
    sel_w = []
    for i, m in enumerate(m_w_list):
        res = evaluation_row(m, f"w_{i}")
        if res: sel_w.append(res)
    note_r = st.text_area("إضافات المربي (اللغة العربية):", placeholder="اكتب هنا مهارات إضافية في اللغة...")

# --- الحساب ---
with tabs[2]:
    st.markdown("<div class='section-head'>المهارات الحسابية</div>", unsafe_allow_html=True)
    m_m_list = ["قراءة وكتابة الأعداد", "العمليات الحسابية الأربع", "حل مسائل كلامية", "التفكير الحسابي والمنطقي"]
    sel_m = []
    for i, m in enumerate(m_m_list):
        res = evaluation_row(m, f"m_{i}")
        if res: sel_m.append(res)
    note_m = st.text_area("إضافات المربي (الحساب):", placeholder="اكتب هنا أي تفاصيل حسابية...")

# --- النمائي ---
with tabs[3]:
    st.markdown("<div class='section-head'>المجالات النمائية والوظيفية</div>", unsafe_allow_html=True)
    m_n_list = ["الإصغاء والتركيز", "الذاكرة واسترجاع المعلومات", "التنظيم وإدارة الوقت", "المهارات الحركية الدقيقة", "التواصل اللغوي والبصري"]
    sel_n = []
    for i, m in enumerate(m_n_list):
        res = evaluation_row(m, f"n_{i}")
        if res: sel_n.append(res)
    note_n = st.text_area("إضافات المربي (المجالات النمائية):", placeholder="اكتب هنا أي ملاحظات وظيفية...")

# === التقرير النهائي ===
st.markdown("---")
if st.button("📄 إصدار التقرير النهائي المدمج"):
    if not student_name: st.error("يرجى إدخال اسم الطالب.")
    else:
        final_report = f"""
🧭 بوصلة مدرسة سلوان الابتدائية الجديدة 🧭
--------------------------------------------------
بيانات الطالب: {student_name} | الهوية: {student_id} | الصف: {student_class}
المربي/ة: {teacher_mrbia} | مركزة التربية الخاصة: مها سرحان
--------------------------------------------------

1. الجانب السلوكي والاجتماعي:
المهارات المحققة: { '، '.join(sel_s) if sel_s else 'لا يوجد' }
إضافات المربي: {note_s if note_s else 'لا يوجد'}

2. الجانب التعليمي (اللغة العربية):
المهارات المحققة: { '، '.join(sel_r + sel_w) if (sel_r + sel_w) else 'لا يوجد' }
إضافات المربي: {note_r if note_r else 'لا يوجد'}

3. الجانب التعليمي (الحساب):
المهارات المحققة: { '، '.join(sel_m) if sel_m else 'لا يوجد' }
إضافات المربي: {note_m if note_m else 'لا يوجد'}

4. المجالات النمائية والوظيفية:
المهارات المحققة: { '، '.join(sel_n) if sel_n else 'لا يوجد' }
إضافات المربي: {note_n if note_n else 'لا يوجد'}

--------------------------------------------------
نظام "بوصلة سلوان" - فكرة وتطوير: مها سرحان
جميع الحقوق محفوظة © مدرسة سلوان الابتدائية الجديدة
"""
        st.text_area("التقرير جاهز للنسخ:", value=final_report, height=450)
        st.success("تم إعداد التوصيف بنجاح.")