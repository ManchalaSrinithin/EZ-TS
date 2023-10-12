def twoSum(self, nums, target):
        s=nums[:]
        l=[]
        nums.sort()
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]+nums[j]==target:
                if nums[i]==nums[j]:
                    l.append(s.index(nums[i]))
                    s[s.index(nums[i])]=-1
                    l.append(s.index(nums[j]))
                    return l
                l.append(s.index(nums[i]))
                l.append(s.index(nums[j]))    
                return l
            elif nums[i]+nums[j]>target:
                j=j-1
            else:
                i=i+1
        return l
l=list(map(int,input().split()))
n=int(input())
print(twosum(l,n))