l=list(map(int,input().split()))
for i in range(max(l),0,-1):
    print(f"{i:2d} | ",end="")
    for j in range(0,len(l)):
        if l[j]>=i:
            print("X",end=' ')
        else:
            print(" ",end=' ')
    print(" ")