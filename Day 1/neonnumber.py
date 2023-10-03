class neon:
    def sum2(k):
        print(k)
        sum1=0
        while k>0:
            rem=k%10
            sum1+=rem
            k=k//10
        c=len(str(sum1))
        if c==1:
            return sum1
        else:
            return sum2(sum1)
n=int(input())
k=pow(n,2)
p=sum2(k)
if p==n:
    print("neon number")
else:
    print("Not a neon number")



        
    
