import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة مدرسة سلوان - التقرير الوصفي الشامل", layout="wide")

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

# --- ميثاق المربي (عزيزي المربي) ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>بين يديك أمانة عظيمة، يرجى تعبئة هذا المسح المهاري بدقة متناهية. تقييمك هو حجر الأساس في بناء مستقبل الطالب التعليمي، فكن دقيقاً، أميناً، وموضوعياً. إن مسؤولية الكلمة هنا هي أمانة مهنية وأخلاقية تجاه الطالب وأسرته.</p>
</div>
""", unsafe_allow_html=True)

# دالة التقييم الذكية
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

living_info = st.text_input("مع من يعيش الطالب؟ (في حال الانفصال)") if f_status == "منفصلون" else ""

# --- 2. التبويبات المهارية (دون أي تغيير في المهارات) ---
tabs = st.tabs(["📖 اللغة العربية", "🧮 الرياضيات", "🤝 الاجتماعي", "❤️ العاطفي", "🎭 السلوكي", "🌟 نقاط القوة"])
opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

with tabs[0]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية</div>", unsafe_allow_html=True)
    ara_r = [smart_eval(t, f"ar_r_{i}", opt_edu) for i, t in enumerate(["تمييز الحروف (اسماً وصوتاً)", "تحليل وتركيب الكلمات", "قراءة جمل مشكولة", "الطلاقة القرائية (نص)", "فهم المقروء (مباشر واستنتاجي)"])]
    ara_w = [smart_eval(t, f"ar_w_{i}", opt_edu) for i, t in enumerate(["المسكة الصحيحة للقلم", "النسخ المنظم (غيباً ونقلاً)", "الكتابة على السطر", "تنظيم الحيز البصري"])]
    ara_e = [smart_eval(t, f"ar_e_{i}", opt_edu) for i, t in enumerate(["التعبير الشفهي الواضح", "سرد قصة منطقياً", "كتابة جملة وصفية", "ترابط الأفكار كتابياً"])]
    ara_s = [smart_eval(t, f"ar_s_{i}", opt_edu) for i, t in enumerate(["الإملاء المنظور", "الإملاء الغيبي", "قواعد الإملاء (تاء، تنوين، همزة)"])]
    obs_ara = st.text_area("ملاحظات إضافية اختيارية للعربي:", key="obs_ara")

with tabs[1]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات</div>", unsafe_allow_html=True)
    mat_m = [smart_eval(t, f"ma_{i}", opt_edu) for i, t in enumerate(["العد والملاءمة (كمية/عدد)", "القيمة المنزلية", "الجمع البسيط", "الجمع مع حمل", "الطرح البسيط", "الطرح مع استلاف", "جداول الضرب", "القسمة البسيطة", "مسائل كلامية (مرحلة واحدة)", "مسائل كلامية (متعددة المراحل)", "الهندسة والقياس"])]
    obs_mat = st.text_area("ملاحظات إضافية اختيارية للرياضيات:", key="obs_mat")

with tabs[2]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي</div>", unsafe_allow_html=True)
    soc_m = [smart_eval(t, f"so_{i}", opt_freq) for i, t in enumerate(["تكوين صداقات", "المشاركة والتعاون الجماعي", "تبادل الأدوار", "حل النزاعات سلمياً", "فهم القواعد الاجتماعية"])]
    obs_soc = st.text_area("ملاحظات إضافية اختيارية للاجتماعي:", key="obs_soc")

with tabs[3]:
    st.markdown("<div class='section-head'>❤️ الجانب العاطفي</div>", unsafe_allow_html=True)
    emo_m = [smart_eval(t, f"em_{i}", opt_freq) for i, t in enumerate(["التعبير عن الذات والمشاعر", "الثقة بالنفس والمبادرة", "تقبل النقد أو الخسارة", "التعاطف مع الآخرين", "ضبط الانفعالات"])]
    obs_emo = st.text_area("ملاحظات إضافية اختيارية للعاطفي:", key="obs_emo")

with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي</div>", unsafe_allow_html=True)
    beh_m = [smart_eval(t, f"be_{i}", opt_freq) for i, t in enumerate(["الالتزام بدستور الصف", "التركيز والاستمرار بالمهمة", "الانتقال بين الفعاليات", "تنظيم الأدوات والحقيبة", "المحافظة على الممتلكات"])]
    obs_beh = st.text_area("ملاحظات إضافية اختيارية للسلوكي:", key="obs_beh")

with tabs[5]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة</div>", unsafe_allow_html=True)
    strengths = st.text_area("مواهب الطالب ومجالات تميزه:", height=150)

# --- توليد التقرير السردي الفقرات ---
if st.button("📄 توليد التقرير الوصفي النهائي"):
    v = "الطالب" if gender == "ذكر" else "الطالبة"
    
    # تحويل المهارات إلى نص فقرات
    ara_text = f"في مهارات اللغة العربية، يلاحظ أن {v} {ara_r[0][1]} مهارة تمييز الحروف، و{ara_r[3][1]} الطلاقة القرائية. أما في الكتابة والنسخ فهو {ara_w[1][1]}، وبالنسبة للإملاء والقواعد {ara_s[2][1]}. {obs_ara}"
    math_text = f"بالانتقال للرياضيات، فإن قدرة {v} على الجمع مع الحمل {mat_m[3][1]}، وفي مهارة الطرح مع الاستلاف {mat_m[5][1]}. كما يظهر مستوى {mat_m[8][1]} في حل المسائل الكلامية. {obs_mat}"
    soc_text = f"من الناحية الاجتماعية والسلوكية، {v} {soc_m[0][1]} يبادر لتكوين الصداقات، ويلتزم بدستور الصف بشكل {beh_m[0][1]}. {obs_soc} {obs_beh}"
    emo_text = f"عاطفياً، يظهر {v} مستوى {emo_m[1][1]} من الثقة بالنفس، و{emo_m[4][1]} يضبط انفعالاته. {obs_emo}"

    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - الإصدار السردي 2026 🧭
--------------------------------------------------
البيانات الشخصية:
الاسم: {s_name} | الصف: {s_class} | ترتيبه بين إخوته الـ {siblings_count}: {student_rank}.

الوصف الأكاديمي:
{ara_text}
{math_text}

الوصف الاجتماعي والعاطفي والسلوكي:
{soc_text}
{emo_text}

نقاط القوة:
{strengths}
--------------------------------------------------
إعداد المربي/ة: {mrbia} | مركزة التربية الخاصة: مها سرحان
مدرسة سلوان الابتدائية الجديدة 2026
شكراً لتعاونكم وأمانتكم المهنية.
"""
    st.text_area("التقرير الوصفي النهائي (جاهز للنسخ):", report, height=600)
    st.success("تم التوليد بنجاح مع الحفاظ على كافة المهارات السابقة.")
