import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_list = words.split()
derp = {}
for i in range(len(word_list)-1):
    if word_list[i] in derp:
        derp[word_list[i]].append(word_list[i+1])
    else:
        derp[word_list[i]] = [word_list[i+1]]

seed_words = [i for i in list(derp.keys()) if "A" <= i <= "Z"]
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

