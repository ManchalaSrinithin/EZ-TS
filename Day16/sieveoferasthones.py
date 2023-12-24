n=int(input())
l=[True for _ in range(n+1)]
for i in range(2,n+1):
    if l[i]==True:
        for j in range(i*i,n+1,i):
                l[j]=False
c=0
for i in range(2,n+1):
    if l[i]==True:
        c+=1
        print(i)
print(c)
        