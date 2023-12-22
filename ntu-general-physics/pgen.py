import random
a = [x + 1 for x in list(range(97))]
random.shuffle(a)
a = sorted(a[0:20])
print(a)

