import streamlit as st
from datetime import date

# إعدادات الصفحة - النسخة الاحترافية (مدرسة سلوان)
st.set_page_config(page_title="بوصلة مدرسة سلوان - الإصدار الذكي", layout="wide")

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
    .stRadio > div { flex-direction: row !important; gap: 15px; }
    </style>
    <div class="footer">فكرة وتطوير: مها سرحان © 2024 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

# --- الترويسة ---
st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان الابتدائية الجديدة</h1>", unsafe_allow_html=True)
st.write(f"**مدير المدرسة:** الأستاذ يحيى نابلسي | **مركزة التربية الخاصة:** مها سرحان")

# === البيانات التعريفية وتحديد الجنس ===
col1, col2, col3 = st.columns(3)
with col1:
    student_name = st.text_input("اسم الطالب/ة:")
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)
with col2:
    student_id = st.text_input("رقم الهوية:")
    student_class = st.text_input("الصف:")
with col3:
    teacher_mrbia = st.text_input("اسم المربي/ة:")
    report_date = st.date_input("تاريخ التقرير:", date.today())

# ميكانيكية الصيغة
prefix = "الطالب" if gender == "ذكر" else "الطالبة"
verb = "يـ" if gender == "ذكر" else "تـ"
pronoun = "لديه" if gender == "ذكر" else "لديها"
he_she = "هو" if gender == "ذكر" else "هي"

# === نقاط القوة ===
st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
strengths = st.text_area(f"بماذا يتميز {prefix}؟ (سلوك، مواهب، مهارات اجتماعية)", placeholder="مثال: طالب مبادر، لديه دافعية عالية، متعاون مع زملائه...")

# دالة التقييم المتدرج
def eval_row(label, key):
    col_t, col_c = st.columns([2.5, 1.5])
    with col_t: st.write(f"**{label}**")
    with col_c: 
        res = st.radio("", ["مستقل", "بوساطة", "دعم كلي", "لا ينفذ"], key=key, horizontal=True, label_visibility="collapsed")
    
    if res == "مستقل": return f"{verb}قوم بـ {label} بشكل مستقل تماماً."
    if res == "بوساطة": return f"{verb}حتاج لوساطة بسيطة أو تلميح لـ {label}."
    if res == "دعم كلي": return f"{verb}حتاج لدعم وتوجيه مكثف لـ {label}."
    return None

st.header("📋 التوصيف الوظيفي")
t1, t2, t3, t4 = st.tabs(["🏛️ السلوكي", "📖 العربية", "🧮 الحساب", "🧠 النمائي"])

# --- السلوكي ---
with t1:
    m_s = ["الالتزام بقوانين الحصة", "المواظبة على إحضار الأدوات", "الاندماج الاجتماعي مع الزملاء", "ضبط النفس عند الغضب", "إتمام المهام التعليمية"]
    sel_s = [eval_row(m, f"s{i}") for i, m in enumerate(m_s)]
    note_s = st.text_area("ملاحظات إضافية (سلوكي):")

# --- العربية ---
with t2:
    m_r = ["قراءة نص مشكول بطلاقة", "فهم الفكرة المركزية للنص", "استنتاج أحداث غير مصرح بها", "النسخ المنظم عن السبورة", "صياغة جملة صحيحة لغوياً"]
    sel_r = [eval_row(m, f"r{i}") for i, m in enumerate(m_r)]
    note_r = st.text_area("ملاحظات إضافية (اللغة العربية):")

# --- الحساب ---
with t3:
    m_m = ["إجراء العمليات الحسابية (الجمع والطرح)", "قراءة وكتابة الأعداد ضمن المنهج", "حل مسائل كلامية بسيطة", "تمييز الأشكال الهندسية"]
    sel_m = [eval_row(m, f"m{i}") for i, m in enumerate(m_m)]
    note_m = st.text_area("ملاحظات إضافية (الحساب):")

# --- النمائي ---
with t4:
    m_n = ["الإصغاء والتركيز خلال الحصة", "تنظيم الأدوات والكتب", "الذاكرة البصرية والسمعية", "التواصل البصري واللفظي", "المهارات الحركية الدقيقة (الكتابة)"]
    sel_n = [eval_row(m, f"n{i}") for i, m in enumerate(m_n)]
    note_n = st.text_area("ملاحظات إضافية (النمائي):")

# === إصدار التقرير ===
st.markdown("---")
if st.button("📄 توليد التقرير النهائي"):
    if not student_name: st.error("يرجى كتابة اسم الطالب أولاً!")
    else:
        # تصفية النتائج
        final_s = " \n ".join([x for x in sel_s if x])
        final_r = " \n ".join([x for x in sel_r if x])
        final_m = " \n ".join([x for x in sel_m if x])
        final_n = " \n ".join([x for x in sel_n if x])

        report_text = f"""
🧭 تقرير "بوصلة مدرسة سلوان" - التوصيف التربوي 🧭
--------------------------------------------------
بيانات الطالب/ة: {student_name} | الصف: {student_class} | التاريخ: {report_date}
المربي/ة: {teacher_mrbia} | مدير المدرسة: يحيى نابلسي
--------------------------------------------------

🌟 نقاط القوة:
{strengths if strengths else 'لم يتم تحديد نقاط قوة خاصة.'}

1. الجانب السلوكي والاجتماعي:
{final_s if final_s else 'لا يوجد مهارات محددة.'}
* إضافات: {note_s if note_s else '---'}

2. الجانب التعليمي (اللغة العربية):
{final_r if final_r else 'لا يوجد مهارات محددة.'}
* إضافات: {note_r if note_r else '---'}

3. الجانب التعليمي (الحساب):
{final_m if final_m else 'لا يوجد مهارات محددة.'}
* إضافات: {note_m if note_m else '---'}

4. المجالات النمائية والوظيفية:
{final_n if final_n else 'لا يوجد مهارات محددة.'}
* إضافات: {note_n if note_n else '---'}

--------------------------------------------------
نظام بوصلة سلوان - إعداد مركزة التربية الخاصة: مها سرحان
جميع الحقوق محفوظة © 2024
"""
        st.text_area("التقرير الجاهز للنسخ:", value=report_text, height=500)
        st.success("تم تحديث الصيغ بنجاح بناءً على جنس الطالب/ة.")
