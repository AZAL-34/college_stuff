import pandas as pd

beverages = pd.DataFrame({
    "Name":[
        "Robert",
        "Melinda",
        "Brenda",
        "Samantha",
        "Melinda",
        "Robert",
        "Melinda",
        "Brenda",
        "Samantha"
    ],
    "Coffee":[
        3,
        0,
        2,
        2,
        0,
        2,
        0,
        1,
        3
    ],
    "Tea":[
        0,
        4,
        2,
        0,
        3,
        0,
        3,
        2,
        0]
})

total_coffee = beverages["Coffee"].sum()
total_tea = beverages["Tea"].sum()

print(f"total coffee drank: {total_coffee}")
print(f"total tea drank: {total_tea}")

res = beverages.groupby(["Name"]).sum()
print(res)