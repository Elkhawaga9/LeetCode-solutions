class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            t = []
            for l in strs:
                t.append(l[i])
            for i in range(1,len(t)):
                if ord(t[i])<ord(t[i-1]):
                    ans+=1
                    break
        return ans
