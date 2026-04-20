import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import gzip
 

class MnistData:
    def __init__(self):
        self.mnist_data = {
            'x_train': None,
            'y_train': None,
            'x_test': None,
            'y_test': None
        }
        # add a lot more lines here...

    def _download(self):
        # add the download code here...
        pass

    def _load_images(self, filename):
        # add the code to load images here...
        pass

    def _load_labels(self, filename):
        # add the code to load labels here...
        pass

    def _one_hot_encode(self, labels, num_classes=10):
        # add the code to one-hot encode labels here...
        pass

    def _normalize(self, x):
        # add the code to normalize pixel values here...
        pass

    def load_data(self):
        # add the code to load and preprocess data here...
        # assign the loaded and preprocessed data to self.mnist_data
        # return (self.mnist_data['x_train'], self.mnist_data['y_train']), (self.mnist_data['x_test'], self.mnist_data['y_test'])   
        pass
