class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def help(idx,idx2):
            if idx2==len(t):
                return 1
            if idx == len(s):
                return 0
            
            if (idx,idx2) in memo:
                return memo[(idx,idx2)]
            Without = help(idx+1,idx2)
            With = 0
            if s[idx]==t[idx2]:
                With = help(idx+1,idx2+1)
            ans = With+Without
            memo[(idx,idx2)] = ans
            return ans
        return help(0,0)

        