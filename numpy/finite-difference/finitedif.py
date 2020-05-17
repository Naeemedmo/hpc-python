import numpy as np
import math
import matplotlib.pyplot as plt

def derivitive(func):
    def evaluate(x):
        delta = x[1:] - x[:-1]
        derv = (func(x[:-1]+delta)-func(x[:-1]-delta))/(2.0*delta)
        return derv
    return evaluate

if __name__ == '__main__':
    d_sin = derivitive(np.sin)
    xi = np.arange(0.,math.pi/2.,0.1)

    plt.plot(xi[:-1],d_sin(xi), label="sin")
    plt.plot(xi[:-1],np.cos(xi[:-1]), label="cos")
    plt.show()
