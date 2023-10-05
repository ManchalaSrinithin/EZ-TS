def generate_sq(n):
    mat=[[0]*n for i in range(n)]
    num=1
    def fill(i,j,num):
        while num<=n*n:
            if i<0 and j==n:
                i=0
                j=n-2
            else:
                if i<0:
                    i=n-1
                if j==n:
                    j=0
            if mat[i][j]:
                i=i+1
                j=j-2
                return fill(i,j,num)
            mat[i][j]=num
            num+=1
            i=i-1
            j=j+1
    fill(n//2,n-1,num)
    return mat
n=int(input())
print(generate_sq(n))

    
        
        