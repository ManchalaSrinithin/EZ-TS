n=int(input())
k=bin(n)
l=k[2::]
print(l)
p=len(l)
print(p)
c=0
n=int(n)
while n>0:
    n=(n&(n-1))
    c+=1
o=p-c
print(o)
if o==0:
    print("Not a power of 4")
    print
if (o&1)!=0:
    print("not a power of 4")
else:
    print("power of 4")
    
