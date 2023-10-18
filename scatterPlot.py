import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Scattered points
ax = plt.axes(projection="3d")

#rand points
x_data = np.random.randint(0, 100, (500))
y_data = np.random.randint(0, 100, (500))
z_data = np.random.randint(0, 100, (500))

ax.scatter(x_data, y_data, z_data)
plt.show()