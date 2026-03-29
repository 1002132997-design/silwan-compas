import streamlit as st
from datetime import date

# إعدادات الصفحة - النسخة التشخيصية الذهبية 2026
st.set_page_config(page_title="بوصلة مدرسة سلوان - المسح المهاري الشامل", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebarViewPort"], div, p, h1, h2, h3, input, label, .stTextArea {
        font-family: 'Cairo', sans-serif; direction: RTL; text-align: right;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; color: #004d40; text-align: center; padding: 10px; font-weight: bold; border-top: 3px solid #009688; z-index: 100; }
    .main-title { color: #00695c; text-align: center; border-bottom: 2px solid #009688; padding-bottom: 10px; margin-top: -10px; }
    .logo-container { text-align: center; margin-bottom: 15px; }
    .section-head { background-color: #e8f5e9; padding: 10px; border-right: 12px solid #2e7d32; border-radius: 5px; color: #1b5e20; font-weight: bold; margin: 25px 0 10px 0; }
    .instruction-box { background-color: #fff9c4; padding: 20px; border-right: 10px solid #fbc02d; border-radius: 10px; color: #5d4037; font-size: 16px; margin-bottom: 25px; line-height: 1.6; }
    .stTabs [data-baseweb="tab-list"] { display: flex; flex-wrap: wrap; gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #f1f8e9; border-radius: 8px; padding: 10px 20px; color: #1b5e20; font-weight: bold; border: 1px solid #c8e6c9; }
    </style>
    <div class="footer">مشروع بوصلة سلوان - إعداد مركزة التربية الخاصة: مها سرحان © 2026 | مدرسة سلوان الابتدائية الجديدة</div>
    """, unsafe_allow_html=True)

# --- قسم الشعار والعنوان (مدمج وآمن) ---
logo_url = "logo.png" # نفترض وجود ملف logo.png بجانب الكود
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image(logo_url, width=200)
    except:
        # رسالة لطيفة في حال عدم وجود الشعار
        st.info("💡 ملاحظة للمربي: يظهر هنا شعار المدرسة الرسمي (logo.png) فور رفعه للمشروع.")
    st.markdown("<h1 class='main-title'>🧭 بوصلة مدرسة سلوان - المسح التشخيصي المهاري</h1>", unsafe_allow_html=True)

# --- ميثاق المربي (عزيزي المربي) ---
st.markdown("""
<div class='instruction-box'>
    <h3>📜 عزيزي المربي / المربية.. رفيق الدرب</h3>
    <p>
    بين يديك أمانة تعبئة هذا الملف بكل مسؤولية؛ فدقتك في رصد المهارات التفصيلية هي التي ستحدد مسار الدعم التربوي للطالب. 
    يرجى تقييم كل مهارة فرعية بناءً على ملاحظتك المباشرة وأدائه الفعلي. تذكر أنك "عين الطالب البصيرة" وأمانة الكلمة أولوية قصوى.
</p>
</div>
""", unsafe_allow_html=True)

# دالة التقييم الذكية (تحافظ على الخيارات متناسبة مع الجيل)
def smart_eval(label, key, options):
    col_t, col_c = st.columns([2, 2.5])
    with col_t: st.markdown(f"**{label}**")
    with col_c: res = st.radio("", options, key=key, horizontal=True, label_visibility="collapsed")
    return label, res

# --- 1. البيانات التعريفية والاجتماعية المفصلة ---
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

# --- 2. التبويبات المهارية التفصيلية (دون أي تغيير في المحتوى) ---
tabs = st.tabs(["📖 اللغة العربية", "🧮 الرياضيات (مفصل)", "🤝 الاجتماعي", "❤️ العاطفي", "🎭 السلوكي", "🌟 نقاط القوة"])

# خيارات متناسبة مع المحور
opt_edu = ["يتقن", "يتقن جزئياً", "يتقن بوساطة", "لم يكتسبها"]
opt_freq = ["دائماً", "غالباً", "أحياناً", "نادراً", "أبداً"]

# --- عربي (مهارات مفصلة) ---
with tabs[0]:
    st.markdown("<div class='section-head'>📚 مهارات اللغة العربية المفصلة</div>", unsafe_allow_html=True)
    
    st.subheader("🖋️ مهارات القراءة")
    ar_read_skills = ["تمييز الحروف (اسماً وصوتاً وحركة)", "تحليل وتركيب الكلمات", "قراءة جمل مشكولة", "الطلاقة القرائية (نص مشكول)", "فهم المقروء الصريح والمباشر", "فهم المقروء الاستنتاجي"]
    ar_read_res = [smart_eval(s, f"ar_r_{i}", opt_edu) for i, s in enumerate(ar_read_skills)]
    
    st.subheader("🖋️ مهارات الكتابة")
    ar_write_skills = ["المسكة الصحيحة للقلم", "النسخ المنظم (غيباً ونقلاً)", "الكتابة على السطر وتنظيم الحيز"]
    ar_write_res = [smart_eval(s, f"ar_w_{i}", opt_edu) for i, s in enumerate(ar_write_skills)]
    
    st.subheader("🗣️ التعبير الشفوي والكتابي")
    ar_exp_skills = ["التعبير الشفهي الواضح بجمل مفيدة", "سرد قصة أو أحداث منطقياً", "كتابة جملة وصفية تامة المعنى"]
    ar_exp_res = [smart_eval(s, f"ar_e_{i}", opt_edu) for i, s in enumerate(ar_exp_skills)]
    
    st.subheader("📝 مهارات الإملاء")
    ar_spell_skills = ["الإملاء المنظور (كلمات مدروسة)", "الإملاء الغيبي (كلمات جديدة)", "قواعد الإملاء (تاء، تنوين، همزة)"]
    ar_spell_res = [smart_eval(s, f"ar_s_{i}", opt_edu) for i, s in enumerate(ar_spell_skills)]
    
    obs_ara = st.text_area("وصف إضافي اختياري لمستوى اللغة العربية:")

# --- رياضيات (مهارات مفصلة - الجمع مع حمل والطرح مع استلاف) ---
with tabs[1]:
    st.markdown("<div class='section-head'>🧮 مهارات الرياضيات المفصلة</div>", unsafe_allow_html=True)
    
    math_skills = [
        "العد والملاءمة (كمية/عدد)", "القيمة المنزلية (آحاد/عشرات/مئات)", 
        "الجمع البسيط العمودي والأفقي", "الجمع مع حمل (إعادة تسمية)", 
        "الطرح البسيط العمودي والأفقي", "الطرح مع استلاف (استقراض)", 
        "حفظ وفهم جداول الضرب", "القسمة كعملية توزيع بالتساوي", 
        "حل مسائل كلامية (مرحلة واحدة)", "حل مسائل كلامية (متعددة المراحل)", 
        "الهندسة والقياس (الأشكال/الساعة/النقود)"
    ]
    math_res = [smart_eval(s, f"ma_{i}", opt_edu) for i, s in enumerate(math_skills)]
    
    obs_mat = st.text_area("وصف إضافي اختياري لمستوى الرياضيات:")

# --- اجتماعي (مهارات مفصلة) ---
with tabs[2]:
    st.markdown("<div class='section-head'>🤝 الجانب الاجتماعي (مهارات التفاعل)</div>", unsafe_allow_html=True)
    soc_skills = ["تكوين صداقات مع الأقران", "المشاركة والتعاون الجماعي", "تبادل الأدوار والانتظار", "حل النزاعات سلمياً", "فهم القواعد الاجتماعية ودستور الصف"]
    soc_res = [smart_eval(s, f"so_{i}", opt_freq) for i, s in enumerate(soc_skills)]
    obs_soc = st.text_area("وصف إضافي للجانب الاجتماعي:")

# --- عاطفي (مهارات مفصلة) ---
with tabs[3]:
    st.markdown("<div class='section-head'>❤️ الجانب العاطفي (النضج والوعي الذاتي)</div>", unsafe_allow_html=True)
    emo_skills = ["التعبير عن الذات والمشاعر لفظياً", "الثقة بالنفس والمبادرة بالعمل", "تقبل النقد أو الخسارة بروح رياضية", "التعاطف مع مشاعر الآخرين", "ضبط الانفعالات عند الغضب"]
    emo_res = [smart_eval(s, f"em_{i}", opt_freq) for i, s in enumerate(emo_skills)]
    obs_emo = st.text_area("وصف إضافي للجانب العاطفي:")

# --- سلوكي (مهارات مفصلة) ---
with tabs[4]:
    st.markdown("<div class='section-head'>🎭 الجانب السلوكي (الانضباط والوظيفة)</div>", unsafe_allow_html=True)
    beh_skills = ["الالتزام بدستور الصف وقوانين المدرسة", "ضبط النفس والتحكم بالانفعالات", "الإصغاء والتركيز خلال الحصة", "الانتقال السلس بين الفعاليات", "تنظيم الحقيبة والاعتناء بالأدوات"]
    beh_res = [smart_eval(s, f"be_{i}", opt_freq) for i, s in enumerate(beh_skills)]
    obs_beh = st.text_area("وصف إضافي للجانب السلوكي:")

# --- نقاط قوة ---
with tabs[5]:
    st.markdown("<div class='section-head'>🌟 نقاط القوة والتميز</div>", unsafe_allow_html=True)
    strengths = st.text_area("ما هي مواهب الطالب أو المجالات التي يبدع فيها؟", height=150)

# --- توليد التقرير المبوب والنهائي (مع أسماء المدير والمركزة) ---
if st.button("📄 توليد التقرير التشخيصي النهائي"):
    v = "الطالب" if gender == "ذكر" else "الطالبة"
    
    # دالة مساعدة لتنسيق الأقسام
    def format_section(title, results, obs=""):
        res_lines = [f"- {label}: ({res})" for label, res in results]
        obs_line = f"\nوصف إضافي: {obs}" if obs else ""
        return f"\n\n[{title}]\n" + "\n".join(res_lines) + obs_line

    # تجميع النتائج
    all_res = [
        format_section("محور اللغة العربية - قراءة وكتابة", ar_read_res + ar_write_res + ar_exp_res + ar_spell_res, obs_ara),
        format_section("محور الرياضيات المفصل", math_res, obs_mat),
        format_section("الجانب الاجتماعي", soc_res, obs_soc),
        format_section("الجانب العاطفي", emo_res, obs_emo),
        format_section("الجانب السلوكي", beh_res, obs_beh)
    ]

    report = f"""
🧭 تقرير بوصلة مدرسة سلوان - المسح التشخيصي المهاري 2026 🧭
--------------------------------------------------
البيانات التعريفية والاجتماعية:
- الاسم: {s_name} | الهوية: {s_id}
- الصف: {s_class} | تاريخ الميلاد: {b_date}
- عدد الإخوة: {siblings_count} | الترتيب بينهم: {student_rank}
- الحالة العائلية: {f_status} | {living_info if living_info else ''}
- التاريخ: {date.today()}

النتائج التفصيلية والمبوبة (بناءً على التقييم المباشر):
{"\n".join(all_res)}

🌟 نقاط القوة والتميز:
{strengths if strengths else 'لم تذكر.'}

--------------------------------------------------
إعداد المربي/ة: {mrbia}
مركزة التربية الخاصة: مها سرحان
مدير المدرسة: يحيى نابلسي
مدرسة سلوان الابتدائية الجديدة 2026

"شكراً لتعاونكم وأمانتكم المهنية في رصد مستوى الطالب."
"""
    # عرض التقرير في صندوق نص جاهز للنسخ
    st.text_area("التقرير الوصفي النهائي (جاهز للنسخ والطباعة):", report, height=650)
    
    # رسالة نجاح مع تنسيق الشعار للطباعة
    st.markdown(f'<div style="text-align:center;"><img src="{logo_url}" width="150"><br><b>تم التوليد بنجاح! جاهز للنقل والطباعة.</b></div>', unsafe_allow_html=True)
    st.success("تم بنجاح! التقرير الآن مبوب ومفصل ويحتوي على كافة الأسماء المطلوبة والشعار.")
