class Solution(object):
    def numberOfSteps(self, num):
        c=0
        while num>=0:
            c+=1
            if num&1!=0:
                num=num^num-1
            else:
                num=num-1
        return c
obj=Solution()
n=int(input())
print(obj.numberOfSteps(n))
    