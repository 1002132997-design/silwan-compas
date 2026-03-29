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
    .section-head { background-color: #e8f5e9; padding: 10px; border-right: 12px solid #2e7d32; border-radius: 5px; color: #1b5e20; font-weight: bold; margin: 25px 0 10px 0; }
    .instruction-box { background-color: #fff9c4; padding: 20px; border-right: 10px solid #fbc02d; border-radius: 10px; color: #5d4037; font-size: 16px; margin-bottom: 25px; line-height: 1.6; }
    .stTabs [data-baseweb="tab-list"] { display: flex; flex-wrap: wrap; gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #f1f8e9; border-radius: 8px; padding: 10px 20px; color: #1b5e20; font-weight: bold; border: 1px solid #c8e6c9; }
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد مركزة التربية الخاصة: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

# --- عرض الشعار والعنوان ---
try:
    st.image("logo.png", width=180)
except:
    st.info("💡 ملاحظة للمربي: يظهر هنا شعار المدرسة الرسمي (logo.png).")

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - المسح التشخيصي الشامل</h1>", unsafe_allow_html=True)

# --- قسم الإرشادات والأمانة المهنية ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>
    بين يديك أمانة عظيمة، فهذا الملف ليس مجرد أوراق تُملأ، بل هو <b>بوصلة</b> تحدد ملامح الطريق التعليمي للطالب. 
    يرجى مراعاة ما يلي عند التعبئة:
    <br>
    <b>1. الدقة والموضوعية:</b> اعتمد في تقييمك على ملاحظاتك المباشرة وأعمال الطالب الفعلية.
    <br>
    <b>2. الأمانة المهنية:</b> تذكر أن الكلمة التي تكتبها أمانة أمام الله وأمام مستقبل الطالب.
    <br>
    <b>3. السرية:</b> هذه المعلومات مخصصة للطواقم المهنية فقط ويُمنع تداولها خارج الإطار المهني.
    <br><br>
    <i>"كن أنت عين الطالب البصيرة التي ترسم له طريق النجاح."</i>
</p>
</div>
""", unsafe_allow_html=True)

# دالة التقييم الذكية
def smart_eval(label, key, options):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return f"- {label}: ({res})"

# --- 1. البيانات التعريفية والاجتماعية ---
st.markdown("<div class='section-head'>📋 أولاً: البيانات التعريفية والاجتماعية</div>", unsafe_allow_html=True)
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
    siblings_count = st.number_input("عدد الإخوة الإجمالي:", min_value=0, step=1)
    student_rank = st.text_input("ترتيب الطالب (مثلاً: الأول، الأخير، الثاني..):")

# حقول إضافية
c4, c5 = st.columns(2)
with c4:
    living_info = st.text_input("مع من يعيش الطالب؟ (في حال الانفصال)") if f_status == "منفصلون" else ""
with c5:
    body_size = st.radio("النمو الجسدي مقارنة بالجيل:", ["مناسب", "أصغر/أنحل", "أكبر/أضخم"])

# --- 2. التبويبات (المسح الكامل) ---
tabs = st.tabs(["🌟 نقاط القوة", "📖 اللغة العربية", "🧮 الرياضيات (مفصل)", "🤝 الاجتماعي والعاطفي", "🎭 السلوكي والنمائي"])

opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

with tabs[0]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("اذكر مواهب الطالب، ذكاءه الاجتماعي، أو أي جوانب تميز أخرى:", height=100)

with tabs[1]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية (مسح شامل)</div>", unsafe_allow_html=True)
    ara_tasks = ["تمييز الحروف وأصواتها", "الطلاقة في القراءة", "فهم المقروء وتحليل النص", "النسخ والكتابة المنظمة", "الإملاء (منظور وغيبي)", "التعبير الشفهي والكتابي"]
    res_ara = [smart_eval(t, f"ara_{i}", opt_edu) for i, t in enumerate(ara_tasks)]

with tabs[2]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات (تفصيل دقيق)</div>", unsafe_allow_html=True)
    math_tasks = [
        "العد والملاءمة (كمية/عدد)", "مفهوم القيمة المنزلية (آحاد/عشرات/مئات)",
        "الجمع العمودي والأفقي (مع حمل)", "الطرح العمودي والأفقي (مع استقراض)",
        "حفظ وفهم جداول الضرب", "حل مسائل كلامية متعددة المراحل"
    ]
    res_mat = [smart_eval(t, f"mat_{i}", opt_edu) for i, t in enumerate(math_tasks)]

with tabs[3]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي والعاطفي</div>", unsafe_allow_html=True)
    soc_tasks = ["بناء علاقات مع الأقران", "التعبير عن المشاعر لفظياً", "الثقة بالنفس والمبادرة", "حل النزاعات سلمياً", "التعاطف مع الآخرين"]
    res_soc = [smart_eval(t, f"soc_{i}", opt_freq) for i, t in enumerate(soc_tasks)]

with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي والنمائي</div>", unsafe_allow_html=True)
    beh_tasks = ["الالتزام بدستور المدرسة", "ضبط النفس والتحكم بالانفعالات", "الإصغاء والتركيز خلال الحصة", "المسكة القلمية والتحكم الحركي", "تنظيم الكتب والأدوات"]
    res_beh = [smart_eval(t, f"beh_{i}", opt_freq) for i, t in enumerate(beh_tasks)]

# --- توليد التقرير النهائي ---
st.markdown("---")
if st.button("📄 توليد المسح التشخيصي الكامل"):
    all_res = "\n".join(res_ara + res_mat + res_soc + res_beh)
    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - الإصدار الشامل 2026 🧭
-----------------------------------------------------------
1. البيانات الأساسية:
- الاسم: {s_name} | الهوية: {s_id} | الصف: {s_class}
- تاريخ الميلاد: {b_date} | الحالة العائلية: {f_status}
- عدد الإخوة: {siblings_count} | ترتيب الطالب: {student_rank}
- النمو الجسدي: {body_size} | {living_info if living_info else ''}

2. 🌟 نقاط القوة والتميز:
{strengths if strengths else 'لم تذكر.'}

3. 📊 نتائج المسح التشخيصي (المهارات):
{all_res}

-----------------------------------------------------------
إعداد المربي/ة: {mrbia} | مركزة التربية الخاصة: مها سرحان
مدير المدرسة: يحيى نابلسي | مدرسة سلوان الابتدائية الجديدة 2026
"تمت التعبئة بأمانة ومسؤولية مهنية"
"""
    st.text_area("التقرير النهائي (جاهز للنسخ والطباعة):", report, height=500)
    st.success("تم تحديث الكود وفصل بيانات الإخوة بنجاح!")
