import streamlit as st
from datetime import date

# إعدادات الصفحة - نسخة مدرسة سلوان الاحترافية 2026
st.set_page_config(page_title="بوصلة مدرسة سلوان - التقرير الشامل", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebarViewPort"], div, p, h1, h2, h3, input, label, .stTextArea {
        font-family: 'Cairo', sans-serif; direction: RTL; text-align: right;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; color: #004d40; text-align: center; padding: 10px; font-weight: bold; border-top: 3px solid #009688; z-index: 100; }
    .main-title { color: #00695c; text-align: center; border-bottom: 2px solid #009688; padding-bottom: 10px; }
    .section-head { background-color: #e0f2f1; padding: 10px; border-right: 10px solid #004d40; border-radius: 5px; color: #004d40; font-weight: bold; margin: 20px 0 10px 0; }
    .stTabs [data-baseweb="tab-list"] { display: flex; flex-wrap: wrap; gap: 5px; }
    .stTabs [data-baseweb="tab"] { background-color: #f1f8e9; border-radius: 8px; padding: 8px 15px; color: #004d40; font-weight: bold; }
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - التقرير التشخيصي الشامل</h1>", unsafe_allow_html=True)

# دالة التقييم الذكية التي تغير الخيارات حسب المحور
def smart_eval(label, key, options, v):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return f"- {label}: {res}"

# --- 1. الملف الشخصي والاجتماعي ---
st.markdown("<div class='section-head'>📋 أولاً: البيانات الشخصية والاجتماعية المفصلة</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    s_name = st.text_input("اسم الطالب/ة الكامل:")
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)
    b_date = st.date_input("تاريخ الميلاد:", date(2015, 1, 1))
with c2:
    s_id = st.text_input("رقم الهوية:")
    s_class = st.text_input("الصف والشعبة:")
    f_status = st.selectbox("الحالة الاجتماعية للوالدين:", ["متزوجون", "منفصلون", "أرمل/ة"])
with c3:
    mrbia = st.text_input("اسم المربي/ة:")
    siblings_count = st.number_input("عدد الإخوة:", min_value=0, step=1)
    rank = st.text_input("ترتيب الطالب بينهم:")

c4, c5 = st.columns(2)
with c4:
    living_with = st.text_input("مع من يعيش الطالب؟ (في حال الانفصال):") if f_status == "منفصلون" else ""
with c5:
    body_desc = st.radio("الحجم الجسدي مقارنة بأبناء الجيل:", ["مناسب تماماً", "أصغر/أنحل", "أكبر/أضخم"])

v = "يـ" if gender == "ذكر" else "تـ"

# --- 2. التبويبات بأسلوب "تفصيل التفصيل" ---
tabs = st.tabs(["🌟 نقاط القوة", "🤝 الاجتماعي والعاطفي", "🎭 السلوكي والنمائي", "📖 التعليمي (عربي)", "🧮 التعليمي (رياضيات)"])

# خيارات متغيرة حسب المحور
opt_social = ["دائماً", "غالباً", "أحياناً", "نادراً"]
opt_edu = ["يتقن بمستوى عالٍ", "يتقن جزئياً", "يحتاج لدعم مكثف", "لم يكتسبها"]
opt_beh = ["ملتزم جداً", "ملتزم غالباً", "يحتاج لتذكير", "صعوبة كبيرة"]

with tabs[0]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("ما الذي يجعل هذا الطالب متميزاً؟ (مواهب، دافعية، ذكاء اجتماعي...)", height=150)

with tabs
