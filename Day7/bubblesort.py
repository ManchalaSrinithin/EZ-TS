l=list(map(int,input().split()))
flag=False
for i in range(1,len(l)-1):
    for j in range(len(l)-i):
        if l[j]>l[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
    if flag==False:
        break
    flag=False
print(l)