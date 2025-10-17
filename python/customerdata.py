import pandas as pd, os

pd.set_option("display.max_rows", 200)

separator = """

=====================================================================================================================================================================================

"""
file = pd.read_csv("C:\\Users\\s2259223\\OneDrive - NCG\\code\\data\\files to read\\customer_data.csv")
first = file.sort_values(by = "JoinDate", ascending = True)
print(first)
print(separator)
youngest = file.sort_values(by = "Age", ascending = True)
print(youngest)
print(separator)
alphabetical = file.sort_values(by = "Name", ascending = True)
print(alphabetical)
print(separator)
country = file.sort_values(by = "Country", ascending = True)
print(country)
print(separator)
print(file)
os.system("pause")