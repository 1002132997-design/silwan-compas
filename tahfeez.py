import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة مدرسة سلوان - المسح المهاري", layout="wide")

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

# --- الشعار والعنوان ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=200) # تأكدي من رفع ملف باسم logo.png
    except:
        st.info("💡 ملاحظة للمربي: يرجى رفع ملف الشعار باسم logo.png")
    st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - المسح التشخيصي المهاري</h1>", unsafe_allow_html=True)

# --- ميثاق المربي ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>
    بين يديك أمانة عظيمة، يرجى تعبئة هذا المسح المهاري بدقة متناهية. 
    تقييمك هو حجر الأساس في بناء مستقبل الطالب التعليمي، فكن دقيقاً، أميناً، وموضوعياً. 
    إن مسؤولية الكلمة هنا هي أمانة مهنية وأخلاقية تجاه الطالب وأسرته.
</p>
</div>
""", unsafe_allow_html=True)

# دالة التقييم
def smart_eval(label, key, options):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return f"- {label}: ({res})"

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

# --- 2. التبويبات المهارية التفصيلية ---
tabs = st.tabs(["📖 اللغة العربية", "🧮 الرياضيات", "🤝 الاجتماعي", "❤️ العاطفي", "🎭 السلوكي", "🌟 نقاط القوة"])

opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

with tabs[0]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية (المسح المهاري)</div>", unsafe_allow_html=True)
    st.subheader("🖋️ مهارات القراءة")
    ara_r = ["تمييز الحروف (اسماً وصوتاً)", "تحليل وتركيب الكلمات", "قراءة جمل مشكولة", "الطلاقة القرائية (نص)", "فهم المقروء (مباشر واستنتاجي)"]
    res_ara_r = [smart_eval(t, f"ar_r_{i}", opt_edu) for i, t in enumerate(ara_r)]
    
    st.subheader("🖋️ مهارات الكتابة")
    ara_w = ["المسكة الصحيحة للقلم", "النسخ المنظم (غيباً ونقلاً)", "الكتابة على السطر", "تنظيم الحيز البصري للدفت"]
    res_ara_w = [smart_eval(t, f"ar_w_{i}", opt_edu) for i, t in enumerate(ara_w)]
    
    st.subheader("🖋️ التعبير الكتابي والشفوي")
    ara_e = ["التعبير الشفوي الواضح", "سرد قصة منطقياً", "كتابة جملة وصفية", "ترابط الأفكار كتابياً"]
    res_ara_e = [smart_eval(t, f"ar_e_{i}", opt_edu) for i, t in enumerate(ara_e)]
    
    st.subheader("🖋️ مهارات الإملاء")
    ara_s = ["الإملاء المنظور", "الإملاء الغيبي", "قواعد الإملاء (تاء، تنوين، همزة)"]
    res_ara_s = [smart_eval(t, f"ar_s_{i}", opt_edu) for i, t in enumerate(ara_s)]

with tabs[1]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات (المسح المهاري)</div>", unsafe_allow_html=True)
    math_tasks = [
        "العد والملاءمة (كمية/عدد)", "القيمة المنزلية (آحاد/عشرات/مئات)", 
        "الجمع البسيط", "الجمع مع حمل", "الطرح البسيط", "الطرح مع استلاف",
        "جداول الضرب", "القسمة البسيطة", "مسائل كلامية (مرحلة واحدة)", 
        "مسائل كلامية (متعددة المراحل)", "الهندسة والقياس"
    ]
    res_mat = [smart_eval(t, f"ma_{i}", opt_edu) for i, t in enumerate(math_tasks)]

with tabs[2]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي (مهارات التفاعل)</div>", unsafe_allow_html=True)
    soc_tasks = ["تكوين صداقات", "المشاركة والتعاون الجماعي", "تبادل الأدوار", "حل النزاعات سلمياً", "فهم القواعد الاجتماعية"]
    res_soc = [smart_eval(t, f"so_{i}", opt_freq) for i, t in enumerate(soc_tasks)]

with tabs[3]:
    st.markdown("<div class='section-head'>❤️ الجانب العاطفي (النضج والوعي)</div>", unsafe_allow_html=True)
    emo_tasks = ["التعبير عن الذات والمشاعر", "الثقة بالنفس والمبادرة", "تقبل النقد أو الخسارة", "التعاطف مع الآخرين", "ضبط الانفعالات"]
    res_emo = [smart_eval(t, f"em_{i}", opt_freq) for i, t in enumerate(emo_tasks)]

with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي (الانضباط والوظيفة)</div>", unsafe_allow_html=True)
    beh_tasks = ["الالتزام بدستور الصف", "التركيز والاستمرار بالمهمة", "الانتقال بين الفعاليات", "تنظيم الأدوات والحقيبة", "المحافظة على الممتلكات"]
    res_beh = [smart_eval(t, f"be_{i}", opt_freq) for i, t in enumerate(beh_tasks)]

with tabs[5]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("ما هي مواهب الطالب أو المجالات التي يبدع فيها؟", height=100)

# --- التقرير النهائي ---
if st.button("📄 توليد المسح المهاري الكامل"):
    all_res = "\n".join(res_ara_r + res_ara_w + res_ara_e + res_ara_s + res_mat + res_soc + res_emo + res_beh)
    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - المسح المهاري الشامل 2026
--------------------------------------------------
البيانات التعريفية:
- الاسم: {s_name} | الصف: {s_class}
- عدد الإخوة: {siblings_count} | الترتيب: {student_rank}
- الحالة العائلية: {f_status}

📊 النتائج التفصيلية:
{all_res}

🌟 نقاط القوة:
{strengths}
--------------------------------------------------
إعداد المربي/ة: {mrbia} | مركزة التربية الخاصة: مها سرحان
مدرسة سلوان الابتدائية الجديدة 2026
شكراً لتعاونكم وأمانتكم المهنية.
"""
    st.text_area("التقرير جاهز:", report, height=450)
    st.success("تم توليد التقرير بنجاح. شكراً!")
