'''class fact:
    def f(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*fact.f(self,n-1)
n=int(input())
obj=fact()
print(obj.f(n))'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
