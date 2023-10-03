#smallest number greater than n with exactly 1 bit diff in binary form
n=int(input())
print(n|n+1)