from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = defaultdict(int)
        tempAns = 0
        ans = 0
        p = 0
        for i in range(n):
            while p<n and d[s[p]]==0:
                d[s[p]]+=1
                tempAns+=1
                p+=1
            ans = max(ans,tempAns)
            d[s[i]]-=1
            tempAns-=1
        return ans