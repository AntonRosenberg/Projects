import numpy as np
import matplotlib.pyplot as plt

class gameOfLife:
    def __init__(self):
        self.state = np.zeros([10,10])

    def showState(self):
        plt.imshow(self.state, cmap='gray')
        plt.show()

    def updateState(self):



