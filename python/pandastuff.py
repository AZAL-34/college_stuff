import pandas, matplotlib.pyplot as plt

file = pandas.read_csv("data_set.csv")
file = file.dropna()
volume = file["Make"].value_counts()
colours = ["#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0", "#FFFFFF", "#FF80C0", "#40C0FF", "#FF80C0"]

# plt.bar(volume["Plug-in Hybrid Electric Vehicle (PHEV)"], volume["Battery Electric Vehicle (BEV)"])
plt.figure(figsize = (8, 5))
volume.plot(kind = "pie", color = colours)
plt.title("cars and all that jazz                     ")
plt.ylabel("")
plt.show()