from matplotlib import pyplot as plt
import numpy as np

def PolyCoefficients(x, coeffs):
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

x = np.linspace(0, 1, 10000)
H = [np.array([1, 0, -3, 2]),
     np.array([0, 0, 3, -2]),
     np.array([0, 1, -2, 1]),
     np.array([0, 0, -1, 1])]

(x0, x1, s0, s1) = map(int, input("Enter f(0), f(1), f'(0), f'(1): ").split())
plt.plot(x, PolyCoefficients(x, x0 * H[0] + 
                                x1 * H[1] + 
                                s0 * H[2] + 
                                s1 * H[3]))
plt.quiver([0, 1], [x0, x1], [0.2, -0.2], [0.2 * s0, -0.2 * s1], angles='xy', scale=2, scale_units='xy')
plt.show()