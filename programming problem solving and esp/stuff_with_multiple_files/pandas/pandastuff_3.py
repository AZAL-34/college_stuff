import pandas as pd, matplotlib.pyplot as plt
data = pd.read_csv("programming problem solving and esp\\actual code\\stuff_with_multiple_files\\pandas\\monthly_temperature_data.csv")

plt.plot(data['Month'], data['Temperature (°C)'], color = '#40c0ff')
plt.title("temperature n allat")
plt.xlabel("month")
plt.ylabel("temperature in °c")
plt.legend(loc = 'upper left')
plt.grid(axis = 'y', linestyle = ':')
plt.show()