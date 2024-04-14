class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = [0 for i in range(26)]
        ans = []
        for i in range(len(s)):
            last[ord(s[i])-97] = i
        #return (last)
        sz = 0
        end = 0
        # if I found that the index equals the last occurrence then this is ok
        # and we should try to find another group that occurrence equals the index
        for i in range(len(s)):
            sz +=1
            end = max(end,last[ord(s[i])-97])
            if end == i:
                ans.append(sz)
                sz = 0
        return ans
        