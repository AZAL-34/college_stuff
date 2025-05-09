import pandas

file = pandas.read_csv("pokedex.csv")
volume = file.shape[0]
print(file.dtypes)

missingno = file.isnull().sum()
print(f"The amount of missing values in each data set: {missingno}")

file = file.dropna()

missingno = file.isnull().sum()
print(f"The amount of missing values in each data set: {missingno}")