from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n =  len(s)
        k = len(p)
        ans = []
        window = s[:k]
        p_count = Counter(p)
        w_count = Counter(window)
        for i in  range(n-k):
            if p_count == w_count:
                ans.append(i)
            w_count[s[i]]-=1
            w_count[s[i+k]]+=1
        if p_count==w_count:
            ans.append(n-k)
        return ans
