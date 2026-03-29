import streamlit as st
from datetime import date

# إعدادات الصفحة - نسخة مدرسة سلوان التشخيصية 2026
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

# --- عرض الشعار والعنوان ---
try:
    st.image("logo.png", width=180)
except:
    st.info("💡 ملاحظة: يظهر هنا شعار المدرسة الرسمي (logo.png).")

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - المسح المهاري الشامل</h1>", unsafe_allow_html=True)

# --- قسم الإرشادات ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>
    بين يديك أمانة تحديد المستوى المهاري للطالب بدقة. يرجى تعبئة التقييم بناءً على <b>الأداء الفعلي</b> للطالب في الصف:
    <br>
    <b>- الأمانة المهنية:</b> التقييم الدقيق هو أول خطوة في تقديم الدعم الصحيح.
    <br>
    <b>- الشمولية:</b> يرجى تقييم كل مهارة فرعية على حدة لرسم خارطة طريق واضحة.
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

# --- 2. المسح المهاري (التبويبات) ---
tabs = st.tabs(["📖 اللغة العربية (بالمهارات)", "🧮 الرياضيات (بالمهارات)", "🌟 نقاط القوة", "🤝 الاجتماعي والعاطفي", "🎭 السلوكي والنمائي"])

opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

with tabs[0]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية التفصيلية</div>", unsafe_allow_html=True)
    st.subheader("🎯 مهارات القراءة والوعي الصوتي")
    ara_read = ["تمييز الحروف وأصواتها", "تركيب الحروف لبناء كلمة", "قراءة كلمات وجمل مشكولة", "الطلاقة القرائية في نص كامل"]
    res_ara_r = [smart_eval(t, f"ar_r_{i}", opt_edu) for i, t in enumerate(ara_read)]
    
    st.subheader("🎯 مهارات الفهم والاستيعاب")
    ara_comp = ["فهم المعنى الصريح والمباشر", "استنتاج أحداث ومعانٍ خفية", "تمييز الفكرة المركزية للنص"]
    res_ara_c = [smart_eval(t, f"ar_c_{i}", opt_edu) for i, t in enumerate(ara_comp)]
    
    st.subheader("🎯 مهارات الكتابة والإملاء")
    ara_write = ["النسخ المنظم والدقيق", "الإملاء المنظور (كلمات مدروسة)", "الإملاء الغيبي (كلمات جديدة)", "تمييز القواعد (تاء، تنوين، همزة)", "صياغة جمل مفيدة للتعبير"]
    res_ara_w = [smart_eval(t, f"ar_w_{i}", opt_edu) for i, t in enumerate(ara_write)]

with tabs[1]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات التفصيلية</div>", unsafe_allow_html=True)
    st.subheader("🔢 الأعداد والعمليات")
    math_num = ["العد والملاءمة (كمية/عدد)", "تمييز القيمة المنزلية (آحاد/عشرات/مئات)", "الجمع البسيط (بدون حمل)", "الجمع مع حمل (إعادة تسمية)", "الطرح البسيط (بدون استقراض)", "الطرح مع استقراض (استلاف)"]
    res_mat_n = [smart_eval(t, f"ma_n_{i}", opt_edu) for i, t in enumerate(math_num)]
    
    st.subheader("🔢 مهارات متقدمة")
    math_adv = ["حفظ وفهم جداول الضرب", "القسمة البسيطة", "حل مسائل كلامية (مرحلة واحدة)", "حل مسائل كلامية (متعددة المراحل)", "فهم مفاهيم الهندسة والقياس"]
    res_mat_a = [smart_eval(t, f"ma_a_{i}", opt_edu) for i, t in enumerate(math_adv)]

with tabs[2]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("ما هي المهارات التي يتفوق فيها الطالب؟", height=100)

with tabs[3]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي والعاطفي</div>", unsafe_allow_html=True)
    soc_tasks = ["بناء علاقات مع الأقران", "التعبير عن المشاعر لفظياً", "الثقة بالنفس والمبادرة", "حل النزاعات سلمياً"]
    res_soc = [smart_eval(t, f"soc_{i}", opt_freq) for i, t in enumerate(soc_tasks)]

with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي والنمائي</div>", unsafe_allow_html=True)
    beh_tasks = ["الالتزام بدستور المدرسة", "ضبط النفس والانفعالات", "الإصغاء والتركيز خلال الحصة", "المسكة القلمية والتحكم الحركي"]
    res_beh = [smart_eval(t, f"beh_{i}", opt_freq) for i, t in enumerate(beh_tasks)]

# --- توليد التقرير النهائي ---
st.markdown("---")
if st.button("📄 توليد المسح المهاري الكامل"):
    all_res = "\n".join(res_ara_r + res_ara_c + res_ara_w + res_mat_n + res_mat_a + res_soc + res_beh)
    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - المسح المهاري 2026 🧭
-----------------------------------------------------------
1. البيانات الأساسية:
- الاسم: {s_name} | الهوية: {s_id} | الصف: {s_class}
- عدد الإخوة: {siblings_count} | ترتيب الطالب: {student_rank}
- التاريخ: {date.today()} | المربي/ة: {mrbia}

2. 🌟 نقاط القوة:
{strengths if strengths else 'لم تذكر.'}

3. 📊 نتائج المسح المهاري التفصيلية:
{all_res}

-----------------------------------------------------------
إعداد: طاقم مدرسة سلوان | مركزة التربية الخاصة: مها سرحان
"تمت التعبئة بأمانة ومسؤولية مهنية"
"""
    st.text_area("التقرير جاهز للنسخ:", report, height=500)
    st.success("تم التحديث! المهارات التعليمية الآن مفصلة بدقة.")
