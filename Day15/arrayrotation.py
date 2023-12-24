'''n=list(map(int,input().split()))
k=int(input())
k=k%len(n)
temp=[]
temp=n[-k:]+n[:-k]
print(temp)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(0,k):
            nums.insert(0,nums.pop())'''
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        for i in range(k):
            temp=nums[-1]
            for j in range(n-1,0,-1):
                nums[j]=nums[j-1]
            nums[0]=temp'''
nums=list(map(int,input().split()))
k=int(input())
if len(nums)==0 or k==0:
    return 
k=k%len(nums)
a=len(nums)-k
nums[:]=nums[a:]+nums[:a]
print(nums)
        
