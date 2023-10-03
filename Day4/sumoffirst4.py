def cse(x):
    if x==0:
        return 0
    return (x+cse(x-1))
print(cse(4))