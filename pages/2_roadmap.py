import streamlit as st

st.title("ML Learning roadmap")

st.write("Select a level to start learning.")

# Buttons for levels
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Basics"):
        st.switch_page("pages/3_basics.py")

with col2:
    if st.button("Algorithms"):
        st.switch_page("pages/4_algorithms.py")

with col3:
    if st.button("ML Engineer"):
        st.switch_page("pages/5_ml_engineer.py")