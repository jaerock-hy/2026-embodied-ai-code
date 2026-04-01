import numpy as np
from three_layer_net import ThreeLayerNet
#import three_layer_net

net = ThreeLayerNet()
x = np.array([1.0, -0.5])
y = net.forward(x)  

print(f'{x} -> {y}')
