class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split()
        l1=reversed(l1)
        return(' '.join(l1))
        
