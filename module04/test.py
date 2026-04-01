import numpy as np

# %%
# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# %%
import matplotlib.pylab as plt

# %%
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

# %%
plt.plot(x, y)
plt.show()

