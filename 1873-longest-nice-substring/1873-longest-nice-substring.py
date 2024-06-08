from collections import Counter
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(x):
            for k in x:
                if (k.islower() and k.upper() not in x):
                    return False
                elif (k.isupper() and k.lower() not in x):
                    return False 
            return True
        ans = ""
        for i in range(len(s)):
            tmp = s[i]
            for j in range(i+1,len(s)):
                tmp+=s[j]
                if isNice(tmp) and len(ans)<len(tmp):
                    ans = tmp
                
        return ans

        