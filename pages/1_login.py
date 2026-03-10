import streamlit as st
import requests

st.title("Login")

username=st.text_input("Username")
password=st.text_input("Password",type="password")

if st.button("Login"):

    res=requests.post(
        "http://localhost:8000/login",
        params={"username":username,"password":password}
    )

    st.write(res.json())
