class maximumrunningtimesofcomputers:
    def maxRunTime(self, n: int, batteries):
        batteries.sort()
        total=sum(batteries)
        while batteries[-1]>total//n:
            n-=1
            total-=batteries.pop()
        return total//n
c=maximumrunningtimesofcomputers()
b=[1,2,3]
print(c.maxRunTime(3,b))