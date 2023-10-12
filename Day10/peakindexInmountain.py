def peakIndexInMountainArray(self, arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if mid>0 and arr[mid]<arr[mid-1]:
            end=mid-1
        elif mid<len(arr) and arr[mid]<arr[mid+1] :
            start=mid+1
        else:
            return mid
