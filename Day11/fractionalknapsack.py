c=int(input())
weights=list(map(int,input().split()))
profits=list(map(int,input().split()))
l=list(zip(weights,profits))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
p=0
for weight,profit in l:
    if weight<=c:
        p=p+profit
        c-=weight
    else:
        p+=c*(profit/weight)
        break
print(p)
        
        
    




























































































































