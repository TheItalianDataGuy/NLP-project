import streamlit as st
from backend import date, positivity, negativity
import plotly.express as px

st.header("Sentiment analysis of a diary")

st.subheader("Positivity")
pos_figure = px.line(x=date, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=date, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)
