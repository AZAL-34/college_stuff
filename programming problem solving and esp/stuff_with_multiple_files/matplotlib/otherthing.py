import numpy as np
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1, 2], [3, 4])
plt.annotate("Peak",
             xy = (2, 4),
             xytext = (2, 5),
             arrowprops = dict(facecolor = "red"))
plt.show()
print("hello")