class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        freq = [['0']*26 for i in range(n)]
        for i in range(n):
            for ch in words[i]:
                freq[i][ord(ch)-ord('a')] = '1'
        masks = []
        for l in freq:
            masks.append(int(''.join(l),2))
        print(masks)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if not (masks[i]&masks[j]):
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
        