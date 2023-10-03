def oneton(n):
    if n==0:
        return
    else:
        oneton(n-1)
        print(n)
n=int(input())
oneton(n)