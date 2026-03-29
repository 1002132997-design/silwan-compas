import streamlit as st
from datetime import date

# إعدادات الصفحة - النسخة التشخيصية العملاقة 2026
st.set_page_config(page_title="بوصلة سلوان - التقرير الشامل", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebarViewPort"], div, p, h1, h2, h3, input, label, .stTextArea {
        font-family: 'Cairo', sans-serif; direction: RTL; text-align: right;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; color: #004d40; text-align: center; padding: 10px; font-weight: bold; border-top: 3px solid #009688; z-index: 100; }
    .main-title { color: #00695c; text-align: center; border-bottom: 2px solid #009688; padding-bottom: 10px; }
    .section-head { background-color: #e0f2f1; padding: 10px; border-right: 10px solid #004d40; border-radius: 5px; color: #004d40; font-weight: bold; margin: 20px 0 10px 0; }
    .stTabs [data-baseweb="tab-list"] { display: flex; flex-wrap: wrap; gap: 5px; }
    .stTabs [data-baseweb="tab"] { background-color: #f1f8e9; border-radius: 8px; padding: 8px 15px; color: #004d40; font-weight: bold; }
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - التقرير التشخيصي الشامل (نسخة التفصيل)</h1>", unsafe_allow_html=True)

# دالة التقييم
def eval_row(label, key, v):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", ["مستقل", "بوساطة بسيطة", "بوساطة مكثفة", "دعم كلي", "لا ينفذ"], key=key, horizontal=True, label_visibility="collapsed")
    
    mapping = {
        "مستقل": f"- {v}قوم بـ {label} باستقلالية تامة.",
        "بوساطة بسيطة": f"- {v}قوم بـ {label} مع حاجة لتلميح بسيط.",
        "بوساطة مكثفة": f"- {v}حتاج لوساطة تعليمية مكثفة لـ {label}.",
        "دعم كلي": f"- {v}عجز عن {label} ويحتاج لمساعدة كاملة.",
        "لا ينفذ": f"- مهارة {label} غير مكتسبة حالياً."
    }
    return mapping[res]

# --- البيانات الأساسية ---
st.markdown("<div class='section-head'>📋 أولاً: الملف الشخصي والاجتماعي</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    s_name = st.text_input("اسم الطالب/ة:")
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)
    b_date = st.date_input("تاريخ الميلاد:", date(2015, 1, 1))
with c2:
    s_id = st.text_input("رقم الهوية:")
    s_class = st.text_input("الصف:")
    f_status = st.selectbox("الوضع العائلية:", ["متزوجون", "منفصلون", "أرمل/ة"])
with c3:
    mrbia = st.text_input("اسم المربي/ة:")
    siblings = st.text_input("عدد الإخوة وترتيبه بينهم:")
    body = st.radio("الحجم الجسدي:", ["مناسب لجيله", "أصغر من جيله", "أكبر من جيله"])

living_info = st.text_input("تفاصيل السكن (مع من يعيش؟):") if f_status == "منفصلون" else ""

v = "يـ" if gender == "ذكر" else "تـ"

# --- التبويبات المفصلة ---
tabs = st.tabs(["🧮 الرياضيات (تفصيل)", "📖 اللغة العربية", "🧠 النمائي والحركي", "🎭 السلوكي والاجتماعي", "🌟 نقاط القوة"])

# --- تبويب الرياضيات المفصل ---
with tabs[0]:
    st.markdown("<div class='section-head'>المهارات الرياضية والحسابية</div>", unsafe_allow_html=True)
    m_list = [
        "العد الآلي تصاعدياً وتنازلياً",
        "تمييز رمز العدد وكتابته بدقة",
        "الملاءمة بين العدد والكمية",
        "مفهوم القيمة المنزلية (آحاد، عشرات، مئات)",
        "إجراء عمليات الجمع (بدون فرط)",
        "إجراء عمليات الجمع (مع فرط)",
        "إجراء عمليات الطرح (بدون استقراض)",
        "إجراء عمليات الطرح (مع استقراض)",
        "حفظ وفهم جداول الضرب",
        "حل مسائل كلامية من مرحلة واحدة",
        "حل مسائل كلامية متعددة المراحل",
        "تمييز الأشكال الهندسية وخصائصها",
        "قراءة الساعة والتعامل مع النقود"
    ]
    res_m = [eval_row(m, f"m_{i}", v) for i, m in enumerate(m_list)]
    m_notes = st.text_area("ملاحظات إضافية في الرياضيات:")

# --- تبويب اللغة العربية ---
with tabs[1]:
    st.markdown("<div class='section-head'>مهارات اللغة والتواصل</div>", unsafe_allow_html=True)
    l_list = [
        "تمييز الحروف اسماً وصوتاً",
        "قراءة كلمات مشكولة بسيطة",
        "قراءة نص وفهم معناه الظاهر",
        "استخراج استنتاجات من النص",
        "النسخ المنظم عن السبورة",
        "الإملاء الغيبي للكلمات المدروسة",
        "صياغة جمل مفيدة شفهياً"
    ]
    res_l = [eval_row(l, f"l_{i}", v) for i, l in enumerate(l_list)]
    l_notes = st.text_area("ملاحظات إضافية في اللغة:")

# --- تبويب النمائي والحركي ---
with tabs[2]:
    st.markdown("<div class='section-head'>المجال النمائي والوظيفي</div>", unsafe_allow_html=True)
    n_list = [
        "الإصغاء والتركيز لفترة كافية",
        "الذاكرة السمعية والبصرية",
        "التواصل البصري مع المعلم",
        "المسكة الصحيحة للقلم",
        "تنظيم الحقيبة والكتب"
    ]
    res_n = [eval_row(n, f"n_{i}", v) for i, n in enumerate(n_list)]
    n_notes = st.text_area("ملاحظات نمائية وصحية (أدوية/حواس):")

# --- تبويب السلوكي ---
with tabs[3]:
    st.markdown("<div class='section-head'>الجانب السلوكي والاجتماعي</div>", unsafe_allow_html=True)
    s_list = [
        "الالتزام بدستور الصف والمدرسة",
        "تقبل الخسارة والانتقاد",
        "بناء علاقات إيجابية مع الزملاء",
        "طلب المساعدة بطريقة لائقة"
    ]
    res_s = [eval_row(s, f"s_{i}", v) for i, s in enumerate(s_list)]
    s_notes = st.text_area("ملاحظات سلوكية إضافية:")

# --- نقاط القوة ---
with tabs[4]:
    st.markdown("<div class='section-head'>🌟 التميز والمواهب</div>", unsafe_allow_html=True)
    strengths = st.text_area("اذكري هنا ما يميز هذا الطالب/ة (مواهب، دافعية، ذكاء اجتماعي):")

# --- إصدار التقرير ---
st.markdown("---")
if st.button("📄 توليد التقرير التشخيصي النهائي"):
    all_res = "\n".join([x for x in (res_m + res_l + res_n + res_s) if x])
    
    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - التشخيص المعمق 2026 🧭
--------------------------------------------------
البيانات الشخصية:
- الاسم: {s_name} | الصف: {s_class}
- تاريخ الميلاد: {b_date} | رقم الهوية: {s_id}
- الوضع العائلي: {f_status} | {living_info}
- عدد الإخوة والترتيب: {siblings}
- الوصف الجسدي: {body}
--------------------------------------------------
🌟 نقاط القوة:
{strengths if strengths else 'لم تذكر.'}

📊 التوصيف الوظيفي والمهارات:
{all_res}

📝 ملاحظات إضافية:
- الرياضيات: {m_notes}
- اللغة العربية: {l_notes}
- النمائي والسلوكي: {n_notes} | {s_notes}
--------------------------------------------------
المربي/ة: {mrbia}
مركزة التربية الخاصة: مها سرحان | مدير المدرسة: يحيى نابلسي
تم التوليد بواسطة "بوصلة سلوان" الذكية 2026 ©
"""
    st.text_area("التقرير جاهز للنسخ والطباعة:", report, height=600)
    st.success("تم التحديث! الآن قسم الرياضيات مفصل وشامل.")
