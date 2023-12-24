def getMinimumOperations(arr):
    o=0
    i=0
    j=len(arr)-1
    while i<=j:
        if arr[i]>arr[i+1]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
            o+=2
        if arr[j]<arr[j-1]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            o+=2
        i+=1
        j-=1
    print(arr)
    return o
arr = [5, 5, 6, 5, 7, 3]
operations = getMinimumOperations(arr)
print(f"Minimum operations to sort the array: {operations}")