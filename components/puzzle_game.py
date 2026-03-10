import streamlit as st
import random

def puzzle():

    questions=[
        ("Which algorithm is used for classification?",
        ["Linear Regression","Logistic Regression","PCA"],
        "Logistic Regression")
    ]

    q=random.choice(questions)

    ans=st.radio(q[0],q[1])

    if st.button("Check"):
        if ans==q[2]:
            st.success("Correct")