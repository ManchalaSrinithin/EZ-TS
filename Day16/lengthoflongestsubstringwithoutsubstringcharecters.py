class lengthoflongestsubstringwithoutsubstringcharecters:
    def lengthOfLongestSubstring(self, s):
        l=0
        le=0
        map1={}
        for r in range(len(s)):
            c=s[r]
            if c in map1 and map1[c]>=l:
                l=map1[c]+1
            else:
                le=max(le,r-l+1)
            map1[c]=r
        return le
obj=lengthoflongestsubstringwithoutsubstringcharecters()
s=input()
print(obj.lengthOfLongestSubstring(s))