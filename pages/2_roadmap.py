import streamlit as st

st.set_page_config(page_title="ML Learning Roadmap", page_icon="🚀", layout="wide")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp{
background: linear-gradient(120deg,#fdf0f3,#e8f0ff,#e0fbfc);
}

/* Center main container */
.block-container{
padding-top:2rem;
padding-bottom:0rem;
max-width:900px;
margin:auto;
}

/* Title */
.title{
text-align:center;
font-size:48px;
font-weight:700;
color:#333;
margin-bottom:5px;
}

/* Subtitle */
.subtitle{
text-align:center;
font-size:20px;
color:#555;
margin-bottom:30px;
}

/* Card layout */
.card{
text-align:center;
padding:15px;
}

/* Image center */
.card img{
display:block;
margin:auto;
}

/* Button */
.stButton>button{
width:100%;
border-radius:10px;
height:45px;
font-size:18px;
font-weight:600;
background:#bde0fe;
color:#222;
border:none;
}

.stButton>button:hover{
background:#cdb4db;
transform:scale(1.04);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">🚀 ML Learning Roadmap</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose your learning stage and start your Machine Learning journey</div>', unsafe_allow_html=True)

# -----------------------------
# CENTERED LEVELS
# -----------------------------
col1, col2, col3 = st.columns(3)

# BASICS
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103832.png", width=110)

    st.markdown("### 📘 Basics")
    st.write("Learn Python, statistics, and ML foundations.")

    if st.button("Start Basics"):
        st.switch_page("pages/3_basics.py")

    st.markdown('</div>', unsafe_allow_html=True)

# ALGORITHMS
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/2920/2920277.png", width=110)

    st.markdown("### ⚙️ Algorithms")
    st.write("Explore ML algorithms like regression, clustering, and trees.")

    if st.button("Explore Algorithms"):
        st.switch_page("pages/4_algorithms.py")

    st.markdown('</div>', unsafe_allow_html=True)

# ML ENGINEER
with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/4149/4149653.png", width=110)

    st.markdown("### 🤖 ML Engineer")
    st.write("Build pipelines, deploy models, and work with real ML systems.")

    if st.button("Become ML Engineer"):
        st.switch_page("pages/5_ml_engineer.py")

    st.markdown('</div>', unsafe_allow_html=True)
