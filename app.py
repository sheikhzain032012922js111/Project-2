import streamlit as st
st.title("NetLab AI")
house_sizes= [650, 800, 1000, 1200, 1500]
house_prices=[70, 90, 110, 130, 160]
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
avg_size = calculate_average(house_sizes)
avg_price = calculate_average(house_prices)
st.write("Average House Size:", avg_size, "sqft")
st.write("Average House Price:", avg_price, "k")
st.subheader("All Houses")
for i in range(len(house_sizes)):
    st.write(f"House {i+1}: {house_sizes[i]} sqft - ${house_prices[i]}k")
st.subheader("Try It Yourself")
new_size = st.slider("Pick a house size(sqft)",min_value=500, max_value=2000, value=1000)
price_per_sqft = avg_price / avg_size
estimated_price = new_size * price_per_sqft
st.write(f"Estimated Price for a {new_size} sqft house: ${estimated_price:.1f}k")
st.subheader("Quick verdict")
if estimated_price < 100:
    st.write("That's a affordable house!")
elif estimated_price < 150:
    st.write("That's a mid range house.")
else:
    st.write("That's an expensive house!")