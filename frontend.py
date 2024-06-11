import streamlit as st
from backend import date, positivity, negativity
import plotly.express as px

st.header("Sentiment analysis of a diary")

st.subheader("Positivity")
figure = px.(x=date, y=positivity, labels={"x": "Positivity", "y": "Date"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=date, y=negativity, labels={"x": "Negativity", "y": "Date"})
st.plotly_chart(figure)
