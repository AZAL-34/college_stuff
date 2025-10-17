import pandas as pd, matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv("files to read\\StudentPerformanceFactors.csv"))
plt.scatter(df["Distance_from_Home"], df["Attendance"])
plt.show()