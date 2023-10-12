def fib(n,dp={}):
    if n in dp:
        return dp[n]
    elif n==0:
        dp[0]=0
        return 0
    elif n==1:
        dp[1]=1
        return 1
    else:
        res=fib(n-1,dp)+fib(n-2,dp)
        dp[n]=res
        return res
n=int(input())
print(fib(n))
        