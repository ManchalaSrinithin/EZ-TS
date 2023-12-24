'''def fun(l,target):
    def backtrack(start,sum1,subset):
        if sum1==target:
            res.append(subset[:])
            return
        if sum1>target or start==len(l):
            return
        subset.append(l[start])
        backtrack(start+1,sum1+l[start],subset)
        subset.pop()
        backtrack(start+1,sum1,subset)
    res=[]
    subset=[]
    backtrack(0,0,[])
    return res
l=[1,4,5,3]
t=10
print(fun(l,t))'''
import random

# Generate 3000 random numbers within the range of -1000 to +1000
random_numbers = [random.randint(-1000, 1000) for _ in range(3000)]

# Sort the list in ascending order
random_numbers.sort()

# If you want the result as a string with one number per line:
result = '\n'.join(map(str, random_numbers))

# If you want the result as a list of numbers:
# result = random_numbers

print(result)
