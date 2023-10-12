def trap(self, height):
    i=0
    j=len(height)-1
    lmax=height[i]
    rmax=height[j]
    res=0
    while i<j:
        if lmax<rmax:
            i+=1
            lmax=max(lmax,height[i])
            res+=lmax-height[i]
        else:
            j-=1
            rmax=max(rmax,height[j])
            res+=rmax-height[j]
    return res
