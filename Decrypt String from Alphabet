class Solution:
    

    def freqAlphabets(self, s: str) -> str:
        def get(s):
            return chr(ord('a') + int(s) - 1)
        
        returned = []
        for i in range(0,len(s)):
            if s[i]=='#':
                returned.pop()
                returned.pop()
                returned.append(get(s[i-2:i]))
            else:
                returned.append(get(s[i]))

        return ''.join(returned)
        
