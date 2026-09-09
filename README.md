# AI Concepts Lab

An interactive Streamlit app that demonstrates four core machine learning concepts using a single small dataset of house sizes and prices.

## What it does

The app loads a dataset of houses (size in sqft, price in $k) and lets you explore how different ML techniques treat that same data:

- **Regression** — fits a line predicting price from size, and shows the price-per-sqft rate and base price.
- **Classification** — lets you set a price threshold to label houses "cheap" or "expensive," then trains a logistic regression model to predict that label.
- **Clustering** — uses K-Means to group houses by size and price without any labels, and lets you adjust the number of clusters.
- **Decision Tree** — trains a decision tree to classify houses as cheap/expensive and visualizes the tree's actual decision splits, with an adjustable max depth.

## Tech stack

- [Streamlit](https://streamlit.io/) — UI framework
- [scikit-learn](https://scikit-learn.org/) — regression, classification, clustering, decision tree models
- [Matplotlib](https://matplotlib.org/) — charts

## Project structure

.
├── app.py # Main Streamlit app, sets up tabs and UI
├── modules/
│ └── data_utils.py # Loads the house dataset
└── README.md


## How to run

1. Install dependencies:

   pip install streamlit matplotlib scikit-learn pandas
   
2. Run the app:

   python -m streamlit run app.py

3. Open the local URL Streamlit prints (usually `http://localhost:8501`).

## Dataset

A small hardcoded set of 12 houses (size in sqft, price in $k), defined in `modules/data_utils.py`. Editing that file's `load_house_data()` function changes the data used across every tab.