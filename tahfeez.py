import streamlit as st
from datetime import date

# إعدادات الصفحة - النسخة الموسعة 2026
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
    .stTabs [data-baseweb="tab-list"] { display: flex; flex-wrap: wrap; gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #f1f8e9; border-radius: 8px; padding: 10px 20px; color: #1b5e20; font-weight: bold; border: 1px solid #c8e6c9; }
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد مركزة التربية الخاصة: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - التقرير التشخيصي الشامل</h1>", unsafe_allow_html=True)

# دالة التقييم الذكية
def smart_eval(label, key, options):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return f"- {label}: ({res})"

# --- البيانات الأساسية ---
st.markdown("<div class='section-head'>📋 أولاً: البيانات الشخصية والاجتماعية</div>", unsafe_allow_html=True)
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
    siblings = st.text_input("عدد الإخوة وترتيبه بينهم:")
    body_size = st.radio("النمو الجسدي:", ["مناسب لجيله", "أصغر من جيله", "أكبر من جيله"])

living_info = st.text_input("تفاصيل السكن (مع من يعيش؟):") if f_status == "منفصلون" else ""
v = "يـ" if gender == "ذكر" else "تـ"

# --- التبويبات المفصلة ---
tabs = st.tabs(["🌟 نقاط القوة", "📖 اللغة العربية (تفصيل)", "🧮 الرياضيات", "🤝 الاجتماعي والعاطفي", "🎭 السلوكي والنمائي"])

# خيارات التقييم
opt_edu = ["يتقن تماماً", "يتقن جزئياً", "يتقن بوسطة", "لم يكتسبها"]
opt_social = ["دائماً", "غالباً", "أحياناً", "نادراً"]

with tabs[0]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("ما الذي يميز هذا الطالب/ة؟ (مواهب، ذكاء اجتماعي، دافعية...)", height=150)

with tabs[1]:
    st.markdown("<div class='section-head'>📚 تفصيل مهارات اللغة العربية</div>", unsafe_allow_html=True)
    
    st.subheader("🎯 مهارات القراءة (الفك وفهم المقروء)")
    q_list = ["تمييز الحروف اسماً وصوتاً", "تركيب أصوات الحروف لبناء كلمة", "الطلاقة في قراءة نص مشكول", "فهم المعنى الصريح للنص", "استنتاج أحداث غير مصرح بها", "تمييز أنواع النصوص (قصة، رسالة...)"]
    res_q = [smart_eval(q, f"q_{i}", opt_edu) for i, q in enumerate(q_list)]
    
    st.subheader("✍️ مهارات الكتابة (الآلية والتنظيم)")
    k_list = ["المسكة الصحيحة للقلم", "النسخ الدقيق عن السبورة/الكتاب", "الكتابة على السطر وبخط واضح", "تنظيم الدفتر وترك مسافات بين الكلمات"]
    res_k = [smart_eval(k, f"k_{i}", opt_edu) for i, k in enumerate(k_list)]
    
    st.subheader("📝 مهارات الإملاء")
    e_list = ["إملاء منظور (كلمات مدروسة)", "إملاء غيبي (كلمات جديدة)", "تمييز التاء المربوطة والمبسوطة", "تمييز التنوين عن النون الساكنة", "كتابة الهمزات بشكل صحيح"]
    res_e = [smart_eval(e, f"e_{i}", opt_edu) for i, e in enumerate(e_list)]
    
    st.subheader("🗣️ مهارات التعبير (الشفهي والكتابي)")
    t_list = ["صياغة جملة مفيدة شفهياً", "ترتيب أحداث قصة منطقياً", "كتابة فقرة عن موضوع معين", "الثروة اللغوية واستخدام مفردات جديدة"]
    res_t = [smart_eval(t, f"t_{i}", opt_edu) for i, t in enumerate(t_list)]

with tabs[2]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات</div>", unsafe_allow_html=True)
    m_list = ["العد والملاءمة (كمية/عدد)", "الجمع والطرح حتى 20", "الجمع والطرح حتى 100 (مع فرط)", "حل مسائل كلامية متعددة المراحل", "القيمة المنزلية (آحاد/عشرات)", "الهندسة والقياس"]
    res_m = [smart_eval(m, f"m_{i}", opt_edu) for i, m in enumerate(m_list)]

with tabs[3]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي والعاطفي</div>", unsafe_allow_html=True)
    s_list = ["بناء علاقات إيجابية مع الزملاء", "التعبير عن المشاعر بوضوح", "طلب المساعدة بطريقة لائقة", "المشاركة في اللعب الجماعي", "الثقة بالنفس والمبادرة"]
    res_s = [smart_eval(s, f"s_{i}", opt_social) for i, s in enumerate(s_list)]

with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي والنمائي</div>", unsafe_allow_html=True)
    n_list = ["الالتزام بقوانين ودستور المدرسة", "ضبط النفس عند الغضب/الإحباط", "الإصغاء والتركيز خلال الحصة", "تنظيم الحقيبة والكتب المدرسية", "المواظبة والحضور المنتظم"]
    res_n = [smart_eval(n, f"n_{i}", opt_social) for i, n in enumerate(n_list)]

# --- توليد التقرير النهائي ---
st.markdown("---")
if st.button("📄 توليد التقرير التشخيصي الشامل"):
    all_res = "\n".join(res_q + res_k + res_e + res_t + res_m + res_s + res_n)
    
    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - الإصدار المفصل 2026 🧭
--------------------------------------------------
البيانات الشخصية:
- الاسم: {s_name} | الصف: {s_class}
- تاريخ الميلاد: {b_date} | رقم الهوية: {s_id}
- الحالة العائلية: {f_status} | {living_info}
- الإخوة والترتيب: {siblings} | النمو الجسدي: {body_size}
--------------------------------------------------
🌟 نقاط القوة:
{strengths if strengths else 'لم تذكر.'}

📊 التوصيف الوظيفي المفصل (المهارات):
{all_res}

--------------------------------------------------
إعداد المربي/ة: {mrbia}
مركزة التربية الخاصة: مها سرحان | مدير المدرسة: يحيى نابلسي
جميع الحقوق محفوظة - مدرسة سلوان الابتدائية الجديدة 2026 ©
"""
    st.text_area("التقرير جاهز للنسخ والطباعة:", report, height=600)
    st.success("تم التحديث! اللغة العربية الآن مقسمة بدقة متناهية.")
