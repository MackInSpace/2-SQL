"""This code is on colab.research.google.com"""

"""import numpy as np
import matplotlib.pyplot as plt"""

"""x1 = [0.1, 0.2, 0.3, 0.4]
y1 = [0.5, 2.2, 3.2, 8.7]
x2 = [0.1, 0.2, 0.3, 0.4]
y2 = [1, 4, 9, 16]

plt.plot(x1, y1, label='first plot')
plt.plot(x2, y2, label='second plot')
plt.legend()"""

"""The NumPy library
Short for Numerical Python

Includes a data structure called an ndarray (n-dimensional array, NumPy array):

Similar to lists, but designed for data science
More efficient storage & access for large amounts of numbers
More built-in functionality for working with numbers"""

"""num = 100
x = np.linspace(0, 20, num)
print(x)"""

"""y = np.random.rand(num)
print(y)"""

"""plt.plot(x, y)"""

#Scatter section

"""import numpy as np
import matplotlib.pyplot as plt"""

"""num = 20
# two-dimensional data array
data = np.random.rand(4, num)
print(data)"""

"""plt.scatter(data[0], data[1], c=data[2], s=data[3]*1000, alpha=0.3, cmap='viridis')
plt.colorbar()  # show color scale"""

"""num = 500
data = np.random.rand(num, num)
plt.imshow(data, cmap='binary')
plt.colorbar()"""

