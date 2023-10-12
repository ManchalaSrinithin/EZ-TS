class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=0
        carea=0
        while i<=j:
            area=(j-i)*min(height[i],height[j])
            carea=max(area,carea)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1  
        return carea     
        
        