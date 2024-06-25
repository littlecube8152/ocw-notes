from code_for_hw02 import *
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
C = 100
R = int(1.05 * C)

def draw_perceptron(data, labels, params = {}, hook = None):
    T = params.get('T', 100)
    d = len(data)
    n = len(data[0])

    th = np.array([[0]] * d)
    th0 = np.array([[0]])
    th_list = []
    th0_list = []

    for i in range(n):
        x = np.array(data[:,i])
        plt.plot(x[0], x[1], ("go" if labels[:,i] == 1 else "ro"))

    for iter in range(T):
        change = False
        for i in range(n):
            x = np.array([data[:,i]])
            y = labels[:,i]
            if np.sign(np.dot(x, th) + th0) != y:
                th0 =th0 + y
                th = th + y * x.T
                change = True

            th_list.append(th)
            th0_list.append(th0)
        if not change:
            break
    return (th_list, th0_list)



ax.set(xlim=[-R, R], ylim=[-R, R], xlabel='X axis', ylabel='Y axis')

def get_line(th, th0):
    
    def solve(x):
        # th[0] * x + th[1] * y + th0 = 0, y = - (th[0] * x + th0) / th[1] 
        return - (th[0,0] * x + th0[0]) / th[1,0]
    
    if abs(th[1]) > 1e-6:
        return [-R, R], [solve(-R), solve(R)]

    elif abs(th[0]) > 1e-6:     
        # approximate vertical line
        return [-th0[0] / th[0,0], -th0[0] / th[0,0]], [-R, R]


def gen_coord():
    return np.random.uniform(low=-5, high=5)
ans = np.array([[gen_coord()], [gen_coord()]])
ans0 = np.array([[gen_coord()]])

# data, labels = gen_flipped_lin_separable(200, 0.1, ans, ans0, 2, C)()
data, labels = gen_lin_separable(200, ans, ans0, 2, C)
th_list, th0_list = draw_perceptron(data, labels)

ansx, ansy = get_line(ans, ans0)
correct = ax.plot(ansx, ansy, 'b')[0]
sep = ax.plot([0, 0], [0, 0], 'k')[0]

# place a text box in upper left in axes coords
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textbox = ax.text(0.05, 0.95, 'iter = $0$', transform=ax.transAxes, fontsize=14,
          verticalalignment='top', bbox=props)

def animate(i):
    textbox.set_text('iter = $' + str(i) + '$')
    x, y = get_line(th_list[i], th0_list[i])
    sep.set_xdata(x)
    sep.set_ydata(y)
    return sep, textbox,

ani = animation.FuncAnimation(fig, animate, interval=25, blit=True, frames=len(th0_list), repeat_delay=1000)

plt.show()
