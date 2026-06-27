import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_json("cleaned_data.json")

# -------------------------
# 1. Device Status Count
# -------------------------
status_count = df["status"].value_counts()
print("Status Count:\n", status_count)

status_count.plot(kind="bar")
plt.title("Device Status Count")
plt.show()

# -------------------------
# 2. Average Temperature
# -------------------------
avg_temp = df["temperature_celsius"].mean()
print("Average Temperature:", avg_temp)

# -------------------------
# 3. City-wise device count
# -------------------------
city_count = df["location_city"].value_counts()
print(city_count)

city_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Devices by City")
plt.show()

# -------------------------
# 4. Temperature Trend (basic)
# -------------------------
df["temperature_celsius"].plot(kind="line")
plt.title("Temperature Trend")
plt.show()
