class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)
n=int(input())
obj=Solution()
for i in range(0,n+1):
    print(obj.fib(i))