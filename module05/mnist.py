import pickle
import numpy as np

from mnist_data import MnistData
import utility

PRETRAINED_MODEL_PATH = 'sample_weight.pkl'

class Mnist: 
    def __init__(self):
        self.data = MnistData()
        (self.x_train, self.y_train), (self.x_test, self.y_test) = self.data.load_data()

        self.net = self._load_network()

    def _load_network(self):
        with open(PRETRAINED_MODEL_PATH, 'rb') as f:
            return pickle.load(f) 
        
    def forward(self, x):
        w1, w2, w3 = self.net['W1'], self.net['W2'], self.net['W3']
        b1, b2, b3 = self.net['b1'], self.net['b2'], self.net['b3']

        a1 = np.dot(x, w1) + b1
        z1 = utility.sigmoid(a1)
        a2 = np.dot(z1, w2) + b2
        z2 = utility.sigmoid(a2)
        a3 = np.dot(z2, w3) + b3
        y = utility.softmax(a3)

        return y
    