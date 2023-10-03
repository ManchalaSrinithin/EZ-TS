'''def m(n):
    if n==1:
        return 1
    else:
        return 2*(m(n-1))+1
n=int(input()) 
print(m(n))'''
'''from itertools import permutations

letters ="1234"
k=int(input())
a = permutations(letters)
y = [' '.join(i) for i in a]
print(y[k-1])
'''
def towerofhanoi(n,source,aux,dest):
    if n==1:
        print("I moved from ",source,"to ",dest)
        return
    else:
        towerofhanoi(n-1,source,dest,aux)
        print("i moves from ",source,"to",dest)
        towerofhanoi(n-1,aux,source,dest)
towerofhanoi(4,'source','aux','dest')
    
    