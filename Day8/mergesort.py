#Merge Sort
def mergesort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        mergesort(left)
        mergesort(right)
        i = j =k= 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k]=left[i]
                i += 1
                k +=1
            else:
                l[k]=right[j]
                j += 1
                k+=1
        while i<len(left):
            l[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            l[k]=right[j]
            k+=1
            j+=1
        return l 
n = list(map(int, input().split()))
start = 0
end = len(n) - 1
n = mergesort(n) 
print(n)