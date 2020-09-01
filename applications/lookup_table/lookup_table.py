import math, random
from time import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


my_dict = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    if (x, y) not in my_dict:
        v = x ** y
        v = math.factorial(v)
        v //= (x+y)
        v %= 982451653
        my_dict[(x, y)] = v
        return v
    else:
        return my_dict[(x, y)]


# Do not modify below this line!
t0 = time()
lap = t0
splits = []
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    if i % 5000 == 0:
        now = time()
        splits.append([now-t0, now-lap])
        lap = now
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
for i in splits:
    print(i)
