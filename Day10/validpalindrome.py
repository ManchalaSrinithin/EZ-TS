def v(s):
    n=len(s)
    def palindrome(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    for i in range(len(s)): 
            p=palindrome(i,i)
            if len(p)>1:
                return True
            pal2=palindrome(i,i+1)
            if len(pal2)>1:
                return True
    return False           
s=input()
print(v(s))