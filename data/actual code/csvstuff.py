import pandas, matplotlib.pyplot as plt
file = pandas.read_csv("data\\files to read\\data2.csv")
df = pandas.DataFrame(file)
df = df.dropna()
pandas.set_option('display.max_rows', None)

plt.scatter(df["Duration"], df["Calories"])
plt.xlabel("Duration")
plt.ylabel("Calories Burned")
plt.title("graph")
plt.show()