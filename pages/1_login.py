import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("User Authentication")

option = st.radio("Select Option", ["Register", "Login"])


# ---------------- REGISTER ----------------

if option == "Register":

    st.subheader("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        st.write("Sending request to server...")

        try:

            res = requests.post(
                f"{API_URL}/register",
                json={
                    "username": username,
                    "password": password
                }
            )

            st.write("Response status:", res.status_code)

            if res.status_code == 200:
                st.success(res.json()["message"])
            else:
                st.error(res.json()["detail"])

        except Exception as e:
            st.error(f"Connection failed: {e}")


# ---------------- LOGIN ----------------

elif option == "Login":

    st.subheader("Login")

    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):

        st.write("Sending request to server...")

        try:

            res = requests.post(
                f"{API_URL}/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            st.write("Response status:", res.status_code)

            if res.status_code == 200:

                data = res.json()

                st.success("Login successful")
                st.write("Welcome:", data["username"])

            else:
                st.error(res.json()["detail"])

        except Exception as e:
            st.error(f"Connection failed: {e}")