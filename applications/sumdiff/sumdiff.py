"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
from time import time

# q = set(range(1, 10))
q = set(range(1, 200))
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

l_comb = {}
r_comb = {}

for i in keys:
    l_val = i[0] + i[1]
    r_val = i[0] - i[1]
    if l_val in l_comb:
        l_comb[l_val].append(i)
    else:
        l_comb[l_val] = [i]
    if r_val in r_comb:
        r_comb[r_val].append(i)
    else:
        r_comb[r_val] = [i]

print(f'combinations found, time: {time() - t0}')
pairs = []

for i in l_comb:
    if i in r_comb:
        for j in l_comb[i]:
            for k in r_comb[i]:
                pairs.append((j, k))

# while i < len(keys):
#     for j in keys[i:]:
#         if comb[keys[i]][0] == comb[j][1]:
#             pairs.append((keys[i], j))
#         if comb[keys[i]][1] == comb[j][0]:
#             pairs.append((j, keys[i]))
#     i += 1
#     if i % 100 == 0:
#         print(i)

# breakpoint()
# for k in comb:
#     for j in comb:
#         if comb[k][0] == comb[j][1]:
#             pairs.append((k, j))

for i in pairs:
    print(f'f({rev_f(i[0][0])}) + f({rev_f(i[0][1])}) = f({rev_f(i[1][0])}) - f({rev_f(i[1][1])})')
    print(f'- - -  {i[0][0]} + {i[0][1]} = {i[1][0]} - {i[1][1]}\n')
