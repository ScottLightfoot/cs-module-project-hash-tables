def no_dups(s):
    used = {}
    out = []
    for i in s.split(" "):
        if i in used:
            pass
        else:
            used[i] = 1
            out.append(i)

    return ' '.join([i for i in out])


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))