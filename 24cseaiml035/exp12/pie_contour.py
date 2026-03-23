import numpy as np
import matplotlib.pyplot as plt

# Sample data for pie chart: market shares or categories
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Others']
sizes = [35, 25, 20, 15, 5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightpink']
explode = (0.1, 0, 0, 0, 0)  # Explode first slice

# Sample data for contour: 2D function Z = sin(sqrt(x^2 + y^2))
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create subplots: pie on left, contour on right
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Pie chart on ax1
wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                   shadow=True, startangle=90)
ax1.set_title('Pie Chart: Programming Language Shares')

# Contour plot on ax2 (filled)
contour = ax2.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.8)
ax2.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5)  # Contour lines
plt.colorbar(contour, ax=ax2)
ax2.set_title('Contour Plot: sin(sqrt(x^2 + y^2))')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

plt.tight_layout()
plt.show()
print("Pie chart and contour plot displayed successfully!")

