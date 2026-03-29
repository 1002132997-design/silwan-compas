import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة مدرسة سلوان - المسح التفصيلي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebarViewPort"], div, p, h1, h2, h3, input, label, .stTextArea {
        font-family: 'Cairo', sans-serif; direction: RTL; text-align: right;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; color: #004d40; text-align: center; padding: 10px; font-weight: bold; border-top: 3px solid #009688; z-index: 100; }
    .main-title { color: #00695c; text-align: center; border-bottom: 2px solid #009688; padding-bottom: 10px; }
    .section-head { background-color: #e8f5e9; padding: 10px; border-right: 12px solid #2e7d32; border-radius: 5px; color: #1b5e20; font-weight: bold; margin: 25px 0 10px 0; }
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد مركزة التربية الخاصة: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

# --- الشعار والعنوان ---
try:
    st.image("logo.png", width=180)
except:
    st.info("💡 ملاحظة: يرجى رفع ملف الشعار باسم logo.png ليظهر هنا وفي التقرير.")

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - المسح التشخيصي المهاري الدقيق</h1>", unsafe_allow_html=True)

# دالة التقييم
def smart_eval(label, key, options):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return label, res

# --- 1. البيانات التعريفية ---
st.markdown("<div class='section-head'>📋 أولاً: البيانات التعريفية</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    s_name = st.text_input("اسم الطالب/ة:")
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)
with c2:
    s_id = st.text_input("رقم الهوية:")
    s_class = st.text_input("الصف والشعبة:")
with c3:
    mrbia = st.text_input("اسم المربي/ة:")
    b_date = st.date_input("تاريخ الميلاد:", date(2015, 1, 1))

# --- 2. المهارات المبوّبة بدقة ---
tabs = st.tabs(["📖 مهارات اللغة العربية", "🧮 مهارات الرياضيات", "🤝 الجانب السلوكي والاجتماعي", "🌟 نقاط القوة"])
opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

with tabs[0]:
    st.markdown("<div class='section-head'>📚 تفاصيل مهارات اللغة العربية</div>")
    ara_r = [smart_eval(s, f"ar_r_{i}", opt_edu) for i, s in enumerate(["تمييز الحروف اسماً وصوتاً", "تحليل الكلمات إلى مقاطع", "تركيب المقاطع لتكوين كلمات", "قراءة جمل مشكولة", "الطلاقة في قراءة نص", "فهم المقروء (مباشر)", "فهم المقروء (استنتاجي)"])]
    ara_w = [smart_eval(s, f"ar_w_{i}", opt_edu) for i, s in enumerate(["المسكة الصحيحة للقلم", "النسخ المنظم للهياكل", "الكتابة على السطر", "الإملاء المنظور", "الإملاء الغيبي", "قواعد الإملاء (تاء/تنوين)"])]
    obs_ara = st.text_area("ملاحظات إضافية للعربي (اختياري):")

with tabs[1]:
    st.markdown("<div class='section-head'>🧮 تفاصيل مهارات الرياضيات</div>")
    math_s = [smart_eval(s, f"ma_{i}", opt_edu) for i, s in enumerate(["العد والملاءمة للكمية", "القيمة المنزلية (آحاد/عشرات)", "الجمع البسيط (بدون حمل)", "الجمع مع حمل", "الطرح البسيط (بدون استلاف)", "الطرح مع استلاف", "حفظ وفهم جداول الضرب", "القسمة البسيطة", "حل مسائل كلامية (مرحلة واحدة)", "حل مسائل كلامية (متعددة)", "مهارات الهندسة والقياس"])]
    obs_mat = st.text_area("ملاحظات إضافية للرياضيات (اختياري):")

with tabs[2]:
    st.markdown("<div class='section-head'>🤝 الجوانب السلوكية والاجتماعية والعاطفية</div>")
    beh_s = [smart_eval(s, f"be_{i}", opt_freq) for i, s in enumerate(["تكوين صداقات مع الأقران", "المشاركة والتعاون الجماعي", "حل النزاعات سلمياً", "الالتزام بدستور الصف", "التركيز والاستمرار بالمهمة", "الثقة بالنفس والمبادرة", "ضبط الانفعالات عند الغضب"])]
    obs_beh = st.text_area("ملاحظات إضافية للجانب السلوكي:")

with tabs[3]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>")
    strengths = st.text_area("تحدث عن مواهب الطالب ومجالات تميزه:", height=150)

# --- توليد التقرير المبوب بالتفصيل الممل ---
if st.button("📄 توليد التقرير المهاري المفصل"):
    def format_list(res_list):
        return "\n".join([f"  - {label}: {res}" for label, res in res_list])

    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - المسح المهاري التفصيلي 2026
--------------------------------------------------
البيانات التعريفية:
- الاسم: {s_name} | الصف: {s_class}
- الهوية: {s_id} | تاريخ الميلاد: {b_date}

📖 مهارات اللغة العربية (تفصيلي):
{format_list(ara_r)}
{format_list(ara_w)}
ملاحظات: {obs_ara if obs_ara else 'لا يوجد'}

🧮 مهارات الرياضيات (تفصيلي):
{format_list(math_s)}
ملاحظات: {obs_mat if obs_mat else 'لا يوجد'}

🤝 الجانب السلوكي والاجتماعي والعاطفي:
{format_list(beh_s)}
ملاحظات: {obs_beh if obs_beh else 'لا يوجد'}

🌟 نقاط القوة والتميز:
{strengths if strengths else 'لم تذكر'}

--------------------------------------------------
إعداد المربي/ة: {mrbia}
مركزة التربية الخاصة: مها سرحان
مدير المدرسة: يحيى نابلسي
مدرسة سلوان الابتدائية الجديدة 2026
"شكراً لتعاونكم وأمانتكم المهنية"
"""
    st.text_area("التقرير الجاهز للنسخ (مبوب بالتفصيل):", report, height=600)
    st.success("تم توليد التقرير بكل مهاراته التفصيلية بنجاح.")
