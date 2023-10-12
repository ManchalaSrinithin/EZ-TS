# Triplet Sum
nums=list(map(int,input().split()))
target=int(input())
nums.sort()
res=[]
for i,a in enumerate(nums):
    if a>target:
        break
    if i>0 and a==nums[i-1]:
        continue
    l,r=i+1,len(nums)-1
    while l<r:
        if nums[i]+nums[l]+nums[r]>target:
            r-=1
        elif nums[i]+nums[l]+nums[r]<target:
            l+=1
        else:
            res.append([nums[i],nums[l],nums[r]])
            l+=1
            r-=1
            while nums[i]==nums[i-1] and l<r:
                l+=1
print(res)