import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from modules.data_utils import load_house_data
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="AI Concepts Lab", layout="wide")
st.title("AI Concepts Lab")

df = load_house_data()

st.subheader("House Dataset")
st.dataframe(df)

st.subheader("Quick Stats")
st.write("Average size:", df["size_sqft"].mean(), "sqft")
st.write("Average price:", df["price_k"].mean(), "k")

st.subheader("Size vs Price")
fig, ax = plt.subplots()
ax.scatter(df["size_sqft"], df["price_k"])
ax.set_xlabel("Size (sqft)")
ax.set_ylabel("Price (k)")
ax.set_title("House Size vs Price")
st.pyplot(fig)

st.subheader("Regression Line")

X = df["size_sqft"].values.reshape(-1, 1)
y = df["price_k"].values

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

fig2, ax2 = plt.subplots()
ax2.scatter(df["size_sqft"], df["price_k"], label="Actual")
ax2.plot(df["size_sqft"], predictions, color="red", label="Predicted")
ax2.set_xlabel("Size (sqft)")
ax2.set_ylabel("Price (k)")
ax2.legend()
st.pyplot(fig2)

st.write("Model says: for every extra sqft, price changes by", round(model.coef_[0], 2), "k")
st.write("Base price (intercept):", round(model.intercept_, 2), "k")

st.subheader("Classification: Cheap vs Expensive")

threshold = st.slider("Expensive threshold (price in k)", 70, 160, 110)

df["is_expensive"] = (df["price_k"] > threshold).astype(int)

X_class = df["size_sqft"].values.reshape(-1, 1)
y_class = df["is_expensive"].values

clf = LogisticRegression()
clf.fit(X_class, y_class)

df["predicted_class"] = clf.predict(X_class)

st.write("Threshold set at:", threshold, "k")
st.dataframe(df[["size_sqft", "price_k", "is_expensive", "predicted_class"]])

fig3, ax3 = plt.subplots()
colors = ["red" if val == 1 else "blue" for val in df["is_expensive"]]
ax3.scatter(df["size_sqft"], df["price_k"], c=colors)
ax3.axhline(y=threshold, color="green", linestyle="--", label="Threshold")
ax3.set_xlabel("Size (sqft)")
ax3.set_ylabel("Price (k)")
ax3.legend()
st.pyplot(fig3)