import pandas as pd

def load_house_data():
    data = {
        "size_sqft": [650, 800, 1000, 1200, 1500, 700, 950, 1100, 1350, 1600, 850, 1250],
        "price_k": [70, 90, 110, 130, 160, 75, 105, 120, 145, 170, 95, 135]
    }
    df = pd.DataFrame(data)
    return df