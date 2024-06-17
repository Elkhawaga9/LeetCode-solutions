class Solution:
    def splitString(self, s: str) -> bool:
        arr = []
        def backtrack(idx,prev):
            if idx==len(s):
                return True
            for j in range (idx,len(s)):
                current = int(s[idx:j+1])
                if prev==1+current and backtrack(j+1,current):
                    return True
            return False


        for i in range(len(s)-1):
            if backtrack(i+1, int(s[:i+1])):
                return True
        return False

        