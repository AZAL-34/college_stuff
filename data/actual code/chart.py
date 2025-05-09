import matplotlib.pyplot as plt, pandas as pd

data = pd.read_csv("files to read\\Example Data C.csv")

x = data["X_values"]
y = data["Y_values"]

plt.figure(figsize = (8, 6))
plt.scatter(x, y, color = "#FF80C0")
plt.title("""
e

""")
plt.xlabel("x")
plt.ylabel("y")
plt.show()