import pandas as pd, matplotlib.pyplot as plt
data = pd.read_csv("programming problem solving and esp\\actual code\\stuff_with_multiple_files\\pandas\\sales_data.csv")

category_sales = data.groupby('Category')['Sales'].sum()
plt.bar(category_sales.index, category_sales.values, color = '#f234ad')
plt.title("sales n allat")
plt.xlabel("category")
plt.ylabel("sales")
plt.xticks(rotation = 45)
plt.show()