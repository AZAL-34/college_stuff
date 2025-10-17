import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("files to read\\Line Graph Data.csv")
df = pd.DataFrame(data)

plt.plot(df["Day"], df["Value"])
plt.xlabel("day")
plt.ylabel("value")
plt.title("some sdort of valeueanms evry daY OE SOMETHINHG")
plt.show()