import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: three distributions (e.g., test scores or measurements)
np.random.seed(42)  # For reproducibility
data1 = np.random.normal(100, 15, 1000)  # Mean 100, std 15
data2 = np.random.normal(90, 10, 1000)   # Mean 90, std 10
data3 = np.random.normal(110, 20, 1000)  # Mean 110, std 20
data = [data1, data2, data3]

# Create subplots: histogram on left, boxplot on right
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Histogram on ax1
ax1.hist(data, bins=30, label=['Group 1', 'Group 2', 'Group 3'], color=['blue', 'red', 'green'], alpha=0.7)
ax1.set_title('Histogram of Distributions')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Boxplot on ax2
box = ax2.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'], patch_artist=True,
                  boxprops=dict(facecolor='lightblue', alpha=0.7),
                  medianprops=dict(color='red'))
ax2.set_title('Boxplot of Distributions')
ax2.set_xlabel('Groups')
ax2.set_ylabel('Value')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
print("Histogram and boxplot displayed successfully!")

