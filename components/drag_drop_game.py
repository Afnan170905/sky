import streamlit as st

def drag_drop_game():

    st.write("Match Algorithm with Category")

    algo=st.selectbox(
    "Algorithm",
    ["Linear Regression","KNN","KMeans"]
    )

    cat=st.selectbox(
    "Category",
    ["Regression","Classification","Clustering"]
    )

    if st.button("Submit"):

        if algo=="Linear Regression" and cat=="Regression":
            st.success("Correct!")
        else:
            st.error("Try again")