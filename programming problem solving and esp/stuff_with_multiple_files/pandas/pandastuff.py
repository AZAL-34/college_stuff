import pandas

file = pandas.read_csv("C:\\Users\\s2259223\\OneDrive - NCG\\code\\programming problem solving and esp\\actual code\\stuff_with_multiple_files\\pandas\\dataset.csv")
df = pandas.DataFrame(file)

# output first 5 rows
print(df.head(5))

print("\n\n\n")

# output data types of all columns
print(df.dtypes)

print("\n\n\n")

# output mean / median / min / max for price / quantity
print("mean price: ")
print(df.loc[:, "Price"].mean())
print("median price: ")
print(df.loc[:, "Price"].median())
print("min price: ")
print(df.loc[:, "Price"].min())
print("max price: ")
print(df.loc[:, "Price"].max())
print("mean quantity: ")
print(df.loc[:, "Quantity"].mean())
print("median quantity: ")
print(df.loc[:, "Quantity"].median())
print("min quantity: ")
print(df.loc[:, "Quantity"].min())
print("max quantity: ")
print(df.loc[:, "Quantity"].max())

print("\n\n\n")

# output all rows above £1
print(df[df["Price"] > 1.0])

print("\n")

# output all rows in north region
print(df[df["Region"] == "North"])

print("\n\n\n")

# group by region
for row in df.groupby("Region"):
    print(row)

print("\n\n\n")

