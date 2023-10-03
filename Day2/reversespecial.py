n=input()
n=list(n)
list1={}
s=',!@#$%^&*()_+{}|:"?></*'
for i in range(len(n)):
    if n[i]==' ':
        list1[i]=n[i]
    if n[i] in s:
        list1[i]=n[i]
p=' '
for c in n:
    if c.isalnum():
        p+=c
p=p[::-1]
for i in list1:
    p = p[:i]+list1[i]+p[i:]
print(p)
