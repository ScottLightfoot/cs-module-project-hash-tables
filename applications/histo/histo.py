import textwrap
from collections import Counter

with open("robin.txt") as f:
    words = f.read()
words = words.lower().split()
derp = Counter(words)
derpy = [(i, j) for i, j in derp.items() if j > 1]
derpy.sort(key = lambda x: x[1])
derpy.reverse()

for i in derpy:
    hist = f'{"#" * i[1]}'
    print(f'{i[0]}: '.ljust(15), hist)
