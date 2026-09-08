import pandas as pd
def load_house_data():
    data = {
        "size_sqft": [650, 800, 1000, 1200, 1500],
        "price_k": [70, 90, 110, 130 , 160]
    }
    df = pd.DataFrame(data)
    return df