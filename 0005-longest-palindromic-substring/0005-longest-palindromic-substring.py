class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        length = 1
        def help(l,r):
            nonlocal ans,length
            while l>=0 and r<n and s[l]==s[r]:
                if length<=r-l+1:
                    ans = s[l:r+1]
                    length = r-l+1
                l-=1
                r+=1
        for i in range(len(s)):
            help(i,i)
            help(i,i+1)
        return ans
        