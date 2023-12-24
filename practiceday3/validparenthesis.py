def generate(n):
    def backtract(s, left, right):
        if len(s) == n*2:
            res.append(s)
            return
        if left < n:
            backtract(s+'(', left+1, right)
        if right < left:
            backtract(s+')', left, right+1)
    res = []
    backtract('', 0, 0)
    return res
    
    
ans = generate(4)
print(ans)