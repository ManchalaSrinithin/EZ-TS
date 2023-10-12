def sortColors(self, nums):
    i=0
    j=0
    k=len(nums)-1
    while i<=k:
        if nums[i]==0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        elif nums[i]==1:
            i+=1
        elif nums[i]==2:
            nums[i],nums[k]=nums[k],nums[i]
            k=k-1


                