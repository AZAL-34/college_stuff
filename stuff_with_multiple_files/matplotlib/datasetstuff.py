import pandas as pd
import matplotlib.pyplot as plt

#1: LOAD THE DATASET
csv = pd.read_csv("data_set.csv")
data = pd.DataFrame(csv)
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", None)
print(data.head(5))

#2: DATA CLEANING
