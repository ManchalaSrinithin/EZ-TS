def letterCombinations(self, digits):
    d={ '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res=[]
    def backtrack(i,curstr):
        if len(curstr)==len(digits):
            res.append(curstr)
            return
        for c in d[digits[i]]:
            backtrack(i+1,curstr+c)
    backtrack(0,'')
    if digits=='':
        return []
    return res
