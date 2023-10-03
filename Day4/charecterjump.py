n=input()
k=int(input())
p=ord(n)+k
if p>122:
    p=(p-122)+96
    print(chr(p))
else:
    print(chr(p))
    