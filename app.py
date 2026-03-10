import streamlit as st

st.set_page_config(
    page_title="Gamified ML Learning Platform",
    page_icon="🤖",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#e3f2fd,#fce4ec,#e8f5e9);
background-attachment: fixed;
}

.main-title{
font-size:110px;
font-weight:bold;
text-align:center;
color:#2E7D32;
}

.sub-title{
font-size:26px;
text-align:center;
color:#555;
margin-bottom:40px;
}

.feature-card{
padding:18px;
border-radius:12px;
background:white;
text-align:center;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
font-size:18px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown(
"<h1 style='text-align:center; font-size:50px; color:#2E7D32;'>🤖 AI Powered ML Learning Platform</h1>",
unsafe_allow_html=True
)


st.markdown(
'<p class="sub-title">Learn Machine Learning through AI, Visualizations and Games</p>',
unsafe_allow_html=True
)


# ---------- HERO SECTION ----------
col1, col2 = st.columns([2,1])

with col1:

    st.write("""
Welcome to the **Gamified Machine Learning Platform** 🎮  

This platform helps beginners understand **Machine Learning concepts**  
through interactive explanations, games, and visual learning tools.
""")

    st.write("")

    # LOGIN BUTTON → OPENS login.py
    if st.button("🔑 Go to Login"):
        st.switch_page("pages/1_login.py")

with col2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2821/2821637.png",
        width=340
    )


# ---------- FEATURES ----------
st.markdown("## 🎮 Platform Features")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<div class="feature-card">🤖 AI Tutor</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="feature-card">📊 Visual Learning</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="feature-card">🎮 ML Games</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="feature-card">📈 Progress Tracking</div>', unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built for Gamified ML Learning 🚀")