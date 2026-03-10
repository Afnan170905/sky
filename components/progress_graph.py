import streamlit as st
import plotly.express as px
import pandas as pd

def progress_chart():

    data={
    "Topic":["Linear Regression","SVM","Clustering"],
    "Score":[80,65,90]
    }

    df=pd.DataFrame(data)

    fig=px.bar(df,x="Topic",y="Score")

    st.plotly_chart(fig)