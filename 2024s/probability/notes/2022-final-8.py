import numpy as np
import math
import matplotlib.pyplot as plt

samples = 2000000
interval = 0.2
N = 200
df = 2

for df in [1]:
    points = {}
    for _ in range(samples):
        samplex = sum(np.random.uniform(-math.sqrt(3) / 2.0, math.sqrt(3) / 2.0, size=N))
        sampley = np.random.binomial(N, 0.5)
        x = math.floor((2 * math.sqrt(N) * samplex / sampley) / interval) + (interval / 2)
        if x not in points:
            points[x] = 0
        points[x] += 1

    X, Y = [], []
    for x, y in points.items():
        X.append(x)
        Y.append(y / samples)
    X, Y = zip(*sorted(zip(X, Y)))

    plt.plot(X, Y, label=f'2 sqrt(n) X/Y (df={df})')

for df in [1]:
    points = {}
    for _ in range(samples):
        x = math.floor(np.random.normal(0, 2.0) / interval) + (interval / 2)
        if x not in points:
            points[x] = 0
        points[x] += 1

    X, Y = [], []
    for x, y in points.items():
        X.append(x)
        Y.append(y / samples)
    X, Y = zip(*sorted(zip(X, Y)))

    plt.plot(X, Y, label=f'2 sqrt(n) X/Y (df={df})')

# points = {}
# n = 500
# p = [0.1, 0.7, 0.15, 0.05]
# for _ in range(samples):
#     if _ % 100000 == 0:
#         print(f"Finished iteration {_}")
#     rv = np.random.multinomial(n, p)
#     q = 0
#     for i in range(len(p)):
#         q += (rv[i] - n * p[i]) ** 2 / (n * p[i])
#     x = math.floor(q / interval) + (interval / 2)
#     if x not in points:
#         points[x] = 0
#     points[x] += 1
# real_mean = 8
# n = 250
# def poisson(lam, x):
#     return np.exp(-lam) * lam ** x / np.math.gamma(x + 1) 
# def partition(x):
#     if x < 6:
#         return 0
#     elif x < 7:
#         return 1
#     elif x < 8:
#         return 2
#     elif x < 9:
#         return 3
#     else:
#         return 4
    
# for _ in range(samples):
#     if _ % 100000 == 0:
#         print(f"Finished iteration {_}")
#     sample = np.random.poisson(real_mean, size=n)
#     mean = np.mean(sample)
#     rv = [0, 0, 0, 0, 0]
#     p =  [0, 0, 0, 0, 0]
#     for x in sample:
#         rv[partition(x)] += 1
#     for x in range(20):
#         p[partition(x)] += poisson(mean, x)

#     p[len(p) - 1] += 1 - sum(p)

#     q = 0
#     for i in range(len(p)):
#         q += (rv[i] - n * p[i]) ** 2 / (n * p[i])
#     x = math.floor(q / interval) + (interval / 2)
#     if x not in points:
#         points[x] = 0
#     points[x] += 1
    
# X, Y = [], []
# for x, y in points.items():
#     X.append(x)
#     Y.append(y / samples)
# X, Y = zip(*sorted(zip(X, Y)))
# plt.plot(X, Y, label=f'Q of Multinomial')

plt.xlabel('Random Variable')
plt.ylabel('Frequency')
plt.title(f'Distributions')
plt.legend()
plt.grid(True) 

plt.show()

