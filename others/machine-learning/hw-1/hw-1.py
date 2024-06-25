import numpy as np
def positive(x, th, th0):
    d = (np.dot(th.T, x) + th0)
    if d == 0:
        return 0
    if d < 0:
        return -1
    return 1


# th = np.array([[3], [4]])
# th0 = 0

ths = np.array([[3, 2, 1],
                [4, 6, 3]])
th0s = np.array([5, 1, 0])
data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
labels = np.transpose([-1, -1, +1, +1, +1])


# A = np.sum(np.array(np.vectorize(lambda x, y: positive(x, th, th0) == y, signature='(n),()->()')(data.T, labels)))
# print(A)

seps = np.vectorize(lambda th, th0 : np.sum(np.array(np.vectorize(lambda x, y: positive(x, th.T, th0) == y, signature='(n),()->()')(data.T, labels))), signature='(n),()->()')(ths.T, th0s)
print(seps)
argmx = np.argmax(seps)
print(ths.T[argmx], th0s[argmx])