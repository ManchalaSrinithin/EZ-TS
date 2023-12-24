from itertools import permutations

letters ="1234"
k=int(input())
a = permutations(letters)
y = [' '.join(i) for i in a]
print(y[k-1])