import pandas as pd
data = pd.read_csv("files to read\\data02.csv")
df = pd.DataFrame(data)
rev = 0
for x in range(len(df)):
    price = df.loc[x]["Price_per_Unit"]
    units = data.loc[x]["Units_Sold"]
    total = price * units
    rev += total
print(f"total revenue: {rev}")