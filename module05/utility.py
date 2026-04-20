## Utility functions for multilayer neural network implementation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x)
    e_x = np.exp(x - c)
    s_x = np.sum(e_x)
    return e_x / s_x