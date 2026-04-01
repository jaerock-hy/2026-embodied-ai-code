import numpy as np

class ThreeLayerNet:
    def __init__(self):
        self.w1 = np.array([[1, 1.23, 0.5], [0.2, 0.34, 0.6]])
        self.w2 = np.array([[1, 0.28], [0.23, 0.44], [0.5, 0.36]])
        self.w3 = np.array([[1, 0.82], [0.43, 0.564]])

        self.b1 = np.array([1, 1, 1])
        self.b2 = np.array([1, 2])
        self.b3 = np.array([1, 2])
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def identity(self, x):
        return x

    def forward(self, x):
        a1 = np.dot(x, self.w1) + self.b1
        z1 = self.sigmoid(a1)
        a2 = np.dot(z1, self.w2) + self.b2
        z2 = self.sigmoid(a2)
        a3 = np.dot(z2, self.w3) + self.b3
        return self.identity(a3)
    
if __name__ == '__main__':
    print('This is a three-layer neural network module.')
    print('You can import this module and use the ThreeLayerNet class to create a neural network instance.')