import pandas as pd

pd.set_option("display.max_rows", None)

data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
df_dropped = df.dropna()
mean_maxpulse = df["Maxpulse"].mean()
df_filled = df["Maxpulse"].fillna(mean_maxpulse)
df_filled = df_filled["Calories"].fillna(98)
df_filled = df_filled.fillna(150)

mean_pulse = df_filled["Pulse"].mean
median_pulse = df_filled["Pulse"].median
max_pulse = df_filled["Pulse"].max
min_pulse = df_filled["Pulse"].min
mean_duration = df_filled["Duration"].mean
median_duration = df_filled["Duration"].median
max_duration = df_filled["Duration"].max
min_duration = df_filled["Duration"].min