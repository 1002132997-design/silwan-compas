import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة مدرسة سلوان - التقرير الوصفي", layout="wide")

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
    st.info("💡 ملاحظة: ارفعي الشعار باسم logo.png ليظهر هنا.")

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - التقرير الوصفي الشامل</h1>", unsafe_allow_html=True)

# --- ميثاق المربي ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>بين يديك أمانة كتابة "قصة نجاح أو تحدي" لطالبك. يرجى وصف المهارات بدقة، فالتفاصيل الصغيرة هي التي تصنع الفارق في التشخيص والدعم.</p>
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
    siblings_count = st.number_input("عدد الإخوة:", min_value=0, step=1)
    student_rank = st.text_input("ترتيب الطالب:")

# --- 2. التبويبات المهارية ---
tabs = st.tabs(["📖 اللغة العربية", "🧮 الرياضيات", "🤝 الاجتماعي", "❤️ العاطفي", "🎭 السلوكي", "🌟 نقاط القوة"])
opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

with tabs[0]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية</div>", unsafe_allow_html=True)
    r1 = [smart_eval(t, f"ar_r_{i}", opt_edu) for i, t in enumerate(["تمييز الحروف", "تحليل الكلمات", "الطلاقة القرائية", "فهم المقروء"])]
    r2 = [smart_eval(t, f"ar_w_{i}", opt_edu) for i, t in enumerate(["مسكة القلم", "النسخ المنظم", "الكتابة على السطر"])]
    r3 = [smart_eval(t, f"ar_e_{i}", opt_edu) for i, t in enumerate(["التعبير الشفوي", "سرد قصة", "ترابط الأفكار"])]
    obs_ara = st.text_area("إضافات وصفية للغة العربية:", key="obs_ara")

with tabs[1]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات</div>", unsafe_allow_html=True)
    m1 = [smart_eval(t, f"ma_{i}", opt_edu) for i, t in enumerate(["العد والملاءمة", "القيمة المنزلية", "الجمع مع حمل", "الطرح مع استلاف", "جداول الضرب", "مسائل كلامية"])]
    obs_mat = st.text_area("إضافات وصفية للرياضيات:", key="obs_mat")

with tabs[2]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي</div>", unsafe_allow_html=True)
    s1 = [smart_eval(t, f"so_{i}", opt_freq) for i, t in enumerate(["تكوين صداقات", "المشاركة الجماعية", "حل النزاعات سلمياً"])]
    obs_soc = st.text_area("إضافات وصفية للجانب الاجتماعي:", key="obs_soc")

with tabs[3]:
    st.markdown("<div class='section-head'>❤️ الجانب العاطفي</div>", unsafe_allow_html=True)
    e1 = [smart_eval(t, f"em_{i}", opt_freq) for i, t in enumerate(["التعبير عن المشاعر", "الثقة بالنفس", "ضبط الانفعالات"])]
    obs_emo = st.text_area("إضافات وصفية للجانب العاطفي:", key="obs_emo")

with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي</div>", unsafe_allow_html=True)
    b1 = [smart_eval(t, f"be_{i}", opt_freq) for i, t in enumerate(["الالتزام بالدستور", "التركيز الصفي", "تنظيم الأدوات"])]
    obs_beh = st.text_area("إضافات وصفية للجانب السلوكي:", key="obs_beh")

with tabs[5]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة</div>", unsafe_allow_html=True)
    strengths = st.text_area("تحدث عن مواهب الطالب وما يميز شخصيته:", height=150)

# --- توليد التقرير السردي ---
if st.button("📄 توليد التقرير الوصفي النهائي"):
    v = "الطالب" if gender == "ذكر" else "الطالبة"
    
    # بناء الفقرات
    p1 = f"يظهر في الجانب الأكاديمي للغة العربية أن {v} {r1[0][1]} مهارة تمييز الحروف، بينما {r1[2][1]} مهارة الطلاقة القرائية. وفيما يخص الكتابة، فإن {v} {r2[1][1]} النسخ المنظم. {obs_ara}"
    
    p2 = f"وفي مهارات الرياضيات، تبين أن القدرة على العد والملاءمة {m1[0][1]}، بينما تبرز الحاجة لدعم في الجمع مع الحمل حيث {v} {m1[2][1]} هذه المهارة، وكذلك الطرح مع الاستلاف الذي {m1[3][1]}. {obs_mat}"
    
    p3 = f"اجتماعياً وعاطفياً، يلاحظ أن {v} {s1[0][1]} يبادر لتكوين الصداقات، و{e1[1][1]} يظهر ثقة بالنفس أثناء المهام. {obs_soc} {obs_emo}"
    
    p4 = f"سلوكياً، يلتزم {v} بدستور الصف بشكل {b1[0][1]}، ويظهر مستوى تركيز {b1[1][1]} خلال الحصص الدراسية. {obs_beh}"

    report = f"""
تقرير وصفي شامل - مدرسة سلوان الابتدائية
---------------------------------------
البيانات التعريفية:
الاسم: {s_name} | الصف: {s_class} | ترتيبه بين إخوته الـ {siblings_count}: {student_rank}.

الجانب الأكاديمي (اللغة العربية والرياضيات):
{p1}
{p2}

الجانب الاجتماعي والعاطفي والسلوكي:
{p3}
{p4}

نقاط القوة والتميز:
{strengths}

---------------------------------------
تحريراً في: {date.today()}
توقيع المربي/ة: {mrbia} | مركزة التربية الخاصة: مها سرحان
"شكراً لجهودكم في رصد مصلحة الطالب"
"""
    st.text_area("التقرير الوصفي السردي (جاهز للنسخ):", report, height=600)
    st.success("تم تحويل التقرير إلى أسلوب سردي وصفي بعيداً عن الروبوتية.")
