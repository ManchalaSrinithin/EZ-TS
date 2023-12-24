def coinchange(coins,amount):
    dp=[[amount+1] *(amount+1) for i in range(len(coins)+1)]
    for i in range(len(coins)+1):
        dp[i][0]=0
    for i in range(1,len(coins)+1):
        for j in range(1,amount+1):
            if coins[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
    return dp[len(coins)][amount] if dp[len(coins)][amount]<=amount else -1

coins=list(map(int,input().split()))
amount=int(input())
print(coinchange(coins,amount))
                
