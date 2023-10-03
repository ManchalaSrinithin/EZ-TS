import random
def isnumisland(x,y,n,l):
    if n[x][y]==0:
        return
    if n[x][y]==1:
        n[x][y]=0
    if x<l-1:
        isnumisland(x+1,y,n,l)
    if y>0:
        isnumisland(x,y-1,n,l)
    if x>0:
        isnumisland(x-1,y,n,l)
    if y<l-1:
        isnumisland(x,y+1,n,l)
n=[[0*5 for i in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        n[i][j]=random.randint(0,1)
for i in range(5):
    for j in range(5):
        print(n[i][j],end=' ')
    print()
c=0
for i in range(5):
    for j in range(5):
        if n[i][j]==1:
            c+=1
            isnumisland(i,j,n,5)
print(c)

        