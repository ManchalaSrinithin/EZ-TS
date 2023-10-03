import random
i=4
j=4
a=[[0]*j for i in range(j)]
for i in range(0,4):
    for j in range(0,4):
        a[i][j]=random.randint(0,1)
for i in range(0,4):
    for j in range(0,4):
        print(a[i][j],end=" ")
    print(" ")
rc_1,vc_1,ldc_1,rdc_1,rc_0,vc_0,ldc_0,rdc_0,ldc,rdc,vc,rc=0,0,0,0,0,0,0,0,0,0,0,0
for i in range(0,4):
    for j in range(0,4):
        if i==j:
            ldc+=a[i][j]
        if i+j==4-1:
            rdc+=a[i][j]
for i in range(0,4):
    sumrow=0
    for j in range(0,4):
        sumrow+=a[i][j]
    if sumrow==0:
        rc_0+=1
    if sumrow==4:
        rc_1+=1
for i in range(0,4):
    columnrow=0
    for j in range(0,4):
        columnrow+=a[j][i]
    if columnrow==0:
        vc_0+=1
    if columnrow==4:
        vc_1+=1
print("1's H count:",rc_1)
print("1's V count:",vc_1)
print("1's ld count:",ldc_1)
print("1's rd count:",rdc_1)
print("0's H count:",rc_0)
print("0's V count:",vc_0)
print("0's ld count:",ldc_0)
print("0's rd count:",rdc_0)

        
        
