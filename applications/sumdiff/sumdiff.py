"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
from time import time

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)

def f(x):
    return x*4 + 6
def rev_f(x):
    return int((x-6)/4)
t0 = time()
r = [f(i) for i in q]

print(f'converted to f(i), time: {time() - t0}')
keys = []

for i in range(len(r)):
    for j in range(len(r)):
        keys.append((r[i], r[j]))
comb = {}
for i in keys:
    comb[i] = (i[0] + i[1], i[0] - i[1])

print(f'combinations found, time: {time() - t0}')
pairs = []
for k in comb:
    for j in comb:
        if comb[k][0] == comb[j][1]:
            pairs.append((k, j))
            print(pairs)
for i in pairs:
    print(f'f({rev_f(i[0][0])}) + f({rev_f(i[0][1])}) = f({rev_f(i[1][0])}) - f({rev_f(i[1][1])})')
    print(f'- - -  {i[0][0]} + {i[0][1]} = {i[1][0]} - {i[1][1]}\n')
