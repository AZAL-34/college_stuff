import pandas as pd, matplotlib.pyplot as plt
data = pd.read_csv("programming problem solving and esp\\actual code\\stuff_with_multiple_files\\pandas\\sales_data.csv")

plt.scatter(data['Ad_Spend'], data['Sales'], color = '#f276d4', alpha = 0.5, edgecolor = '#f2c4d3')
plt.title("ads")
plt.xlabel("ad spend")
plt.ylabel("sales")
plt.grid(True)
plt.show()