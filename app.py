import streamlit as st
from modules.data_utils import load_house_data
st.set_page_config(page_title="AI Concepts Lab", layout="wide")
st.title("AI Concepts Lab")
df = load_house_data()
st.subheader("House Dataset")
st.dataframe(df)
st.subheader("Quick Stats")
st.write("Average size:", df["size_sqft"].mean(), "sqft")
st.write("Average price:", df["price_k"].mean(), "k")