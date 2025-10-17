import numpy as np
import matplotlib.pyplot as plt
matrix = np.random.rand(10, 10)
plt.imshow(matrix, cmap = "cool")
plt.colorbar()
plt.show()