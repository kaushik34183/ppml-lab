import matplotlib .pyplot as plt
x=[1,2,3,4,5]
y=[5,6,7,8,9]
plt.scatter(x,y,color='b',label="scatter points")
plt.title("scatter plot")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.legend()
plt.show()
