import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data for 3D surface: Z = sin(sqrt(x^2 + y^2))
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 3D surface plot
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Wireframe overlay for detail
ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.5, alpha=0.3)

# Labels and title
ax.set_title('3D Surface Plot: sin(√(x² + y²))')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z = sin(√(x² + y²))')

# Colorbar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20)

plt.show()
print("3D surface plot displayed successfully! Rotate the view interactively.")

