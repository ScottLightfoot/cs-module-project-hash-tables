from collections import Counter

order_of_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R',
                 'I', 'S', 'D', 'L', 'W', 'U', 'G',
                 'F', 'B', 'M', 'Y', 'C', 'P', 'K',
                 'V', 'Q', 'J', 'X', 'Z']

with open("ciphertext.txt") as f:
    words = f.read()

letters = [i for i in words if "A" <= i <= "Z"]
derp = Counter(letters)
derpy = [(i, j) for i, j in derp.items()]
derpy.sort(key = lambda x: x[1])
derpy.reverse()

cipher = {}
for i in range(26):
    cipher[derpy[i][0]] = order_of_freq[i]
decoded = [cipher[i] if "A" <= i <= "Z" else i for i in words]
out = ''.join(decoded)

print(out)
