n=int(input())
c=0
n=abs(n)
while n:
    n=n&(n-1)
    c+=1
print(c)
