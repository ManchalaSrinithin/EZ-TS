#Merge Sort
def mergesort(l,invers):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        li=mergesort(left,invers)
        ri=mergesort(right,invers)
        i = j =k= 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k]=left[i]
                i += 1
                k +=1
            else:
                l[k]=right[j]
                j += 1
                k+=1
                invers+=len(left)-i
        while i<len(left):
            l[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            l[k]=right[j]
            k+=1
            j+=1
        return li+ri+invers
    return 0
n = list(map(int, input().split()))
start = 0
end = len(n) - 1
x = mergesort(n,0) 
print(x)  
print(n)

# Worst Case , Average and Best case is O(n logn)