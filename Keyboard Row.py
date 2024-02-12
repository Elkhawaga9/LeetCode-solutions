class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fiRow = 'qwertyuiopQWERTYUIOP'
        secRow = 'asdfghjklASDFGHJKL'
        thRow = 'zxcvbnmZXCVBNM'
        ans = []
        for word in words:
            f = True
            for ch in word:
                if ch not in fiRow:
                    f = False
                    break
            if f== True:
                ans.append(word)

        
        for word in words:
            f2 = True
            for ch in word:
                if ch not in secRow:
                    f2 = False
                    break
            if f2 == True:
                ans.append(word)


        for word in words:
            f3 = True
            for ch in word:
                if ch not in thRow:
                    f3 = False
                    break
            if f3== True:
                ans.append(word)
        return ans

        
