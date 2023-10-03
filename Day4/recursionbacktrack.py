def cse(x):
    if x==0:
        return 0
    print(x)
    print(cse(x-1))
    print(x)
    return 18
cse(4)