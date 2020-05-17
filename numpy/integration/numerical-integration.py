import numpy as np
import math

def middleRiemannSum(func):
    def evaluate(x):
        xprim = (x[1:] + x[:-1])/2.0
        delta = x[1:] - x[:-1]
        rsum = np.sum(func(xprim)*delta)
        return rsum
    return evaluate

if __name__ == '__main__':

    riemann_sin = middleRiemannSum(np.sin)
    refvalue = 1.00

    deltax = 1.0
    xi = np.arange(0.,math.pi/2.,deltax)
    difference = refvalue - riemann_sin(xi)
    print('Sum:{} ,with delta: {}, Diff:{}'.format(riemann_sin(xi),deltax,difference))

    deltax = 0.5
    xi = np.arange(0.,math.pi/2.,deltax)
    difference = refvalue - riemann_sin(xi)
    print('Sum:{} ,with delta: {}, Diff:{}'.format(riemann_sin(xi),deltax,difference))

    deltax = 0.1
    xi = np.arange(0.,math.pi/2.,deltax)
    difference = refvalue - riemann_sin(xi)
    print('Sum:{} ,with delta: {}, Diff:{}'.format(riemann_sin(xi),deltax,difference))

    deltax = 0.01
    xi = np.arange(0.,math.pi/2.,deltax)
    difference = refvalue - riemann_sin(xi)
    print('Sum:{} ,with delta: {}, Diff:{}'.format(riemann_sin(xi),deltax,difference))

    deltax = 0.001
    xi = np.arange(0.,math.pi/2.,deltax)
    difference = refvalue - riemann_sin(xi)
    print('Sum:{} ,with delta: {}, Diff:{}'.format(riemann_sin(xi),deltax,difference))
