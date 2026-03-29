import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة مدرسة سلوان - المسح التشخيصي", layout="wide")

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
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد مركزة التربية الخاصة: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

# --- الشعار والعنوان ---
try:
    st.image("logo.png", width=180)
except:
    st.info("💡 ملاحظة للمربي: يرجى رفع ملف الشعار باسم logo.png ليظهر هنا.")

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - المسح التشخيصي المهاري</h1>", unsafe_allow_html=True)

# --- ميثاق المربي ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>بين يديك أمانة تعبئة هذا الملف بكل مسؤولية؛ فدقتك في رصد المهارات هي التي ستحدد مسار الدعم التربوي للطالب. تذكر أنك "عين الطالب البصيرة" وأمانة الكلمة أولوية.</p>
</div>
""", unsafe_allow_html=True)

# دالة التقييم
def smart_eval(label, key, options):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return label, res

# --- 1. البيانات التعريفية ---
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
    student_rank = st.text_input("ترتيب الطالب بين إخوته:")

# --- 2. التبويبات المهارية المفصلة ---
tabs = st.tabs(["📖 اللغة العربية", "🧮 الرياضيات", "🤝 الاجتماعي", "❤️ العاطفي", "🎭 السلوكي", "🌟 نقاط القوة"])
opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

# --- عربي ---
with tabs[0]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية المفصلة</div>", unsafe_allow_html=True)
    ara_skills = [
        "تمييز الحروف (اسماً وصوتاً)", "تحليل وتركيب الكلمات", "قراءة جمل مشكولة", 
        "الطلاقة القرائية (نص)", "فهم المقروء (مباشر واستنتاجي)", "المسكة الصحيحة للقلم", 
        "النسخ المنظم (غيباً ونقلاً)", "الكتابة على السطر", "التعبير الشفهي الواضح", 
        "سرد قصة منطقياً", "كتابة جملة وصفية", "الإملاء المنظور والغيبي", "قواعد الإملاء (تاء، تنوين، همزة)"
    ]
    ara_res = [smart_eval(s, f"ar_{i}", opt_edu) for i, s in enumerate(ara_skills)]
    obs_ara = st.text_area("وصف إضافي لمستوى العربي (اختياري):")

# --- رياضيات ---
with tabs[1]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات المفصلة</div>", unsafe_allow_html=True)
    math_skills = [
        "العد والملاءمة (كمية/عدد)", "القيمة المنزلية (آحاد/عشرات/مئات)", "الجمع البسيط", 
        "الجمع مع حمل", "الطرح البسيط", "الطرح مع استلاف", "جداول الضرب", 
        "القسمة البسيطة", "مسائل كلامية (مرحلة واحدة)", "مسائل كلامية (متعددة المراحل)", "الهندسة والقياس"
    ]
    math_res = [smart_eval(s, f"ma_{i}", opt_edu) for i, s in enumerate(math_skills)]
    obs_mat = st.text_area("وصف إضافي لمستوى الرياضيات (اختياري):")

# --- اجتماعي ---
with tabs[2]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي (مهارات التفاعل)</div>", unsafe_allow_html=True)
    soc_skills = ["تكوين صداقات مع الأقران", "المشاركة والتعاون الجماعي", "تبادل الأدوار والانتظار", "حل النزاعات سلمياً", "فهم القواعد الاجتماعية"]
    soc_res = [smart_eval(s, f"so_{i}", opt_freq) for i, s in enumerate(soc_skills)]
    obs_soc = st.text_area("وصف إضافي للجانب الاجتماعي:")

# --- عاطفي ---
with tabs[3]:
    st.markdown("<div class='section-head'>❤️ الجانب العاطفي (النضج والوعي)</div>", unsafe_allow_html=True)
    emo_skills = ["التعبير عن الذات والمشاعر", "الثقة بالنفس والمبادرة", "تقبل النقد أو الخسارة", "التعاطف مع الآخرين", "ضبط الانفعالات"]
    emo_res = [smart_eval(s, f"em_{i}", opt_freq) for i, s in enumerate(emo_skills)]
    obs_emo = st.text_area("وصف إضافي للجانب العاطفي:")

# --- سلوكي ---
with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي (الانضباط والوظيفة)</div>", unsafe_allow_html=True)
    beh_skills = ["الالتزام بدستور وقوانين الصف", "التركيز والاستمرار بالمهمة", "الانتقال السلس بين الفعاليات", "تنظيم الأدوات والحقيبة", "المحافظة على الممتلكات"]
    beh_res = [smart_eval(s, f"be_{i}", opt_freq) for i, s in enumerate(beh_skills)]
    obs_beh = st.text_area("وصف إضافي للجانب السلوكي:")

# --- نقاط قوة ---
with tabs[5]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("ما هي مواهب الطالب أو المجالات التي يبدع فيها؟", height=150)

# --- توليد التقرير المبوب ---
if st.button("📄 توليد المسح المهاري المبوب"):
    def format_section(title, results, obs):
        lines = [f"\n[ {title} ]"]
        lines.extend([f"- {label}: {val}" for label, val in results])
        if obs: lines.append(f"وصف إضافي: {obs}")
        return "\n".join(lines)

    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - المسح المهاري الشامل 2026
--------------------------------------------------
البيانات التعريفية:
- الاسم: {s_name} | الصف: {s_class}
- عدد الإخوة: {siblings_count} | الترتيب: {student_rank}
- التاريخ: {date.today()}

{format_section("محور اللغة العربية", ara_res, obs_ara)}
{format_section("محور الرياضيات", math_res, obs_mat)}
{format_section("الجانب الاجتماعي", soc_res, obs_soc)}
{format_section("الجانب العاطفي", emo_res, obs_emo)}
{format_section("الجانب السلوكي", beh_res, obs_beh)}

🌟 نقاط القوة والتميز:
{strengths}
--------------------------------------------------
إعداد المربي/ة: {mrbia} | مركزة التربية الخاصة: مها سرحان
مدرسة سلوان الابتدائية الجديدة 2026
شكراً لتعاونكم وأمانتكم المهنية.
"""
    st.text_area("التقرير النهائي (مبوب ومنظم):", report, height=600)
    st.success("تم توليد التقرير المبوب بنجاح!")
