import pandas as pd, matplotlib.pyplot as plt

csv = pd.read_csv("earthquakes.csv")
quakes = pd.DataFrame(csv)

scatter = plt.scatter(quakes["longitude"], quakes["latitude"], c = quakes["mag"], cmap = "RdYlBu_r", marker = ".", s = 3 ** quakes["mag"])
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Earthquakes (higher magnitude = bigger)")
plt.colorbar(scatter, label = "Magnitude")
plt.show()