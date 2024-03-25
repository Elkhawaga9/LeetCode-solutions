class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        s = set()
        s.add(word[0])
        p = 1
        tmp = 0
        ans = 0
        for i in range(n):
            while p<n and len(s)<=5 and ord(word[p]) >= ord(word[p-1]):
                if len(s)==0:
                    s.add(word[p-1])
                s.add(word[p])
                p+=1
                tmp+=1
            if len(s)== 5:
                ans = max(ans,tmp)
            s.clear()
            tmp = 1
            p+=1
        return ans