'''str1=input()
i=0
j=len(str1)-1
while i<j:
    if str1[i]!=str1[j]:
        print("Not palindrome")
        break
    i=i+1
    j=j-1
else:
    print("Palindrome")'''
def p(i,j,n):
    if i<j:
        if n[i]==n[j]:
            return p(i+1,j-1,n)
        else:
            return False
    return True


        
    