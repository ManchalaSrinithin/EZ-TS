class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        max=0
        length=0
        out=" "
        res=" "
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    if s[i:j]==s[j:i:-1]:
                        res=s[i:j+1]
            length=len(res)
            if length>max:
                max=length
                out=res
        return out
