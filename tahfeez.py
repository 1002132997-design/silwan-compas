import streamlit as st
from datetime import date

# إعدادات الصفحة - نسخة 2026 الشاملة
st.set_page_config(page_title="بوصلة مدرسة سلوان - الملف التشخيصي", layout="wide")

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
    .section-head { background-color: #e0f2f1; padding: 10px; border-right: 6px solid #00796b; border-radius: 5px; color: #004d40; font-weight: bold; margin: 20px 0 10px 0; }
    </style>
    <div class="footer">تطوير: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - الملف التشخيصي الشامل</h1>", unsafe_allow_html=True)

# === 1. البيانات الشخصية والاجتماعية ===
st.markdown("<div class='section-head'>📋 البيانات الشخصية والاجتماعية</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    student_name = st.text_input("اسم الطالب/ة:")
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)
    birth_date = st.date_input("تاريخ الميلاد:", date(2015, 1, 1))
with c2:
    student_id = st.text_input("رقم الهوية:")
    student_class = st.text_input("الصف:")
    social_status = st.selectbox("الوضع العائلي للوالدين:", ["متزوجون", "منفصلون", "أرمل/ة"])
with c3:
    teacher_name = st.text_input("اسم المربي/ة:")
    num_siblings = st.number_input("عدد الإخوة:", min_value=0, step=1)
    rank_siblings = st.text_input("ترتيب الطالب بين إخوته:")

# تفاصيل إضافية بناءً على الوضع العائلي
living_with = ""
if social_status == "منفصلون":
    living_with = st.text_input("مع من يعيش الطالب؟ (الأم/الأب/بالتناوب):")

# === 2. الحالة الجسدية ===
st.markdown("<div class='section-head'>👤 النمو الجسدي والحركي</div>", unsafe_allow_html=True)
body_size = st.radio("حجم الطالب مقارنة بأبناء جيله:", ["مناسب جداً", "أصغر من جيله", "أكبر من جيله"], horizontal=True)

# === 3. نقاط القوة ===
st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
strengths = st.text_area("ما الذي يميز الطالب/ة؟", placeholder="اكتبي هنا مهارات الطالب الاجتماعية أو مواهبه...")

# ميكانيكية الصيغة
verb = "يـ" if gender == "ذكر" else "تـ"
prefix = "الطالب" if gender == "ذكر" else "الطالبة"

# دالة التقييم
def eval_row(label, key):
    col_t, col_c = st.columns([2, 2])
    with col_t: st.write(f"**{label}**")
    with col_c: res = st.radio("", ["مستقل", "بوساطة", "دعم كلي", "لا ينفذ"], key=key, horizontal=True, label_visibility="collapsed")
    if res == "مستقل": return f"{verb}قوم بـ {label} بشكل مستقل."
    if res == "بوساطة": return f"{verb}حتاج لوساطة لـ {label}."
    if res == "دعم كلي": return f"{verb}حتاج لدعم مكثف لـ {label}."
    return None

st.markdown("<div class='section-head'>📊 التقييم الوظيفي</div>", unsafe_allow_html=True)
t1, t2 = st.tabs(["📚 المجالات التعليمية", "🤝 المجال السلوكي والنمائي"])

with t1:
    st.subheader("اللغة العربية والحساب")
    # تم إصلاح السطر 75 هنا بدقة:
    m_list = ["قراءة نص وتحليله", "النسخ والكتابة المنظمة", "حل مسائل حسابية", "فهم التعليمات المركبة"]
    res_t1 = [eval_row(m, f"t1_{i}") for i, m in enumerate(m_list)]

with t2:
    st.subheader("السلوك والنمو")
    m_list2 = ["الالتزام بالقوانين", "التواصل مع الزملاء", "التركيز لفترة طويلة", "التنظيم الذاتي"]
    res_t2 = [eval_row(m, f"t2_{i}") for i, m in enumerate(m_list2)]

# === 4. توليد التقرير ===
if st.button("📄 إصدار التقرير النهائي"):
    f_t1 = "\n".join([x for x in res_t1 if x])
    f_t2 = "\n".join([x for x in res_t2 if x])
    
    report = f"""
تقرير بوصلة سلوان التشخيصي (2026)
----------------------------------
الاسم: {student_name} | الجنس: {gender}
تاريخ الميلاد: {birth_date} | الصف: {student_class}
الوضع العائلي: {social_status} {"(يعيش مع: " + living_with + ")" if living_with else ""}
عدد الإخوة: {num_siblings} | الترتيب: {rank_siblings}
الحجم الجسدي: {body_size} مقارنة بأبناء جيله.
----------------------------------
🌟 نقاط القوة:
{strengths}

📊 التوصيف الوظيفي:
{f_t1}
{f_t2}
----------------------------------
إعداد المربي/ة: {teacher_name}
بإشراف: الأستاذ يحيى نابلسي | مركزة التربية الخاصة: مها سرحان
"""
    st.text_area("التقرير جاهز للنسخ:", report, height=400)
    st.success("تم التحديث! الرابط سيعمل الآن بشكل مثالي.")
