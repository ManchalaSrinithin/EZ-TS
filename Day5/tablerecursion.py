def table(k,n):
    if k==11:
        return
    else:
        print(n,"*",k,"=",n*k)
        return table(k+1,n)
n=int(input())
table(1,n)