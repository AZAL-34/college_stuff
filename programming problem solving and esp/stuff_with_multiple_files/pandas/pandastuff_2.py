import pandas as pd, matplotlib.pyplot as plt
data = pd.read_csv("sales_data.csv")
data['Date'] = pd.to_datetime(data['Date'])

plt.plot(data['Date'], data['Sales'], color = '#ff80c1')
plt.title("sales n allat but BETTER")
plt.xlabel("date")
plt.ylabel("sales")
plt.legend(loc = 'upper left')
plt.grid(axis = 'y', linestyle = ':')
plt.show()