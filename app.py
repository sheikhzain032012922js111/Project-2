import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from modules.data_utils import load_house_data
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier, plot_tree

st.set_page_config(page_title="AI Concepts Lab", layout="wide")
st.title("AI Concepts Lab")

df = load_house_data()

with st.sidebar:
    st.header("Dataset")
    st.dataframe(df)
    st.metric("Average size", f"{df['size_sqft'].mean():.0f} sqft")
    st.metric("Average price", f"{df['price_k'].mean():.0f}k")

tab1, tab2, tab3, tab4 = st.tabs(["Regression", "Classification", "Clustering", "Decision Tree"])

with tab1:
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

    col1, col2 = st.columns(2)
    col1.metric("Price change per sqft", f"{model.coef_[0]:.2f}k")
    col2.metric("Base price (intercept)", f"{model.intercept_:.2f}k")

with tab2:
    st.subheader("Classification: Cheap vs Expensive")

    threshold = st.slider("Expensive threshold (price in k)", 70, 160, 110)

    df["is_expensive"] = (df["price_k"] > threshold).astype(int)

    X_class = df["size_sqft"].values.reshape(-1, 1)
    y_class = df["is_expensive"].values

    clf = LogisticRegression()
    clf.fit(X_class, y_class)
    df["predicted_class"] = clf.predict(X_class)

    st.dataframe(df[["size_sqft", "price_k", "is_expensive", "predicted_class"]])

    fig3, ax3 = plt.subplots()
    colors = ["red" if val == 1 else "blue" for val in df["is_expensive"]]
    ax3.scatter(df["size_sqft"], df["price_k"], c=colors)
    ax3.axhline(y=threshold, color="green", linestyle="--", label="Threshold")
    ax3.set_xlabel("Size (sqft)")
    ax3.set_ylabel("Price (k)")
    ax3.legend()
    st.pyplot(fig3)

with tab3:
    st.subheader("Clustering: Grouping Similar Houses")

    n_clusters = st.slider("Number of clusters", 2, 4, 2)

    X_cluster = df[["size_sqft", "price_k"]].values

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_cluster)

    st.dataframe(df[["size_sqft", "price_k", "cluster"]])

    fig4, ax4 = plt.subplots()
    ax4.scatter(df["size_sqft"], df["price_k"], c=df["cluster"], cmap="viridis")
    centers = kmeans.cluster_centers_
    ax4.scatter(centers[:, 0], centers[:, 1], c="red", marker="X", s=200, label="Centers")
    ax4.set_xlabel("Size (sqft)")
    ax4.set_ylabel("Price (k)")
    ax4.legend()
    st.pyplot(fig4)

with tab4:
    st.subheader("Decision Tree: Cheap vs Expensive")

    max_depth = st.slider("Max tree depth", 1, 4, 2)

    tree_clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    tree_clf.fit(X_class, y_class)
    df["tree_prediction"] = tree_clf.predict(X_class)

    st.dataframe(df[["size_sqft", "price_k", "is_expensive", "tree_prediction"]])

    fig5, ax5 = plt.subplots(figsize=(10, 6))
    plot_tree(
        tree_clf,
        feature_names=["size_sqft"],
        class_names=["cheap", "expensive"],
        filled=True,
        rounded=True,
        fontsize=10,
        ax=ax5
    )
    plt.tight_layout()
    st.pyplot(fig5)