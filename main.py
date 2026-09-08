# practice code 9/8/2026
house_sizes= [650, 800, 1000, 1200, 1500]
house_prices=[70, 90, 110, 130, 160]
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
avg_size = calculate_average(house_sizes)
avg_price = calculate_average(house_prices)
print("Average House Size:", avg_size)
print("Average House Price:", avg_price)
for i in range(len(house_sizes)):
    size = house_sizes[i]
    price = house_prices[i]
    print(f"House {i+1}: {size} sqft - ${price}k")
