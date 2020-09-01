import re

def word_count(s):
    s = re.sub('[^a-zA-Z\' ]+', ' ', s)
    low_s = s.lower()
    my_dict = {}
    out = low_s.split()
    for w in out:
        if w in my_dict:
            my_dict[w] += 1
        else:
            my_dict[w] = 1
    return my_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))