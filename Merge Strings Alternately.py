class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer =""
        min_length = min(len(word1),len(word2))
        for i in range (min_length):
            answer+=word1[i]
            answer+=word2[i]

        if len(word1)>min_length:
            answer+=word1[min_length:]

        if len(word2)>min_length:
            answer+=word2[min_length:]
        return answer
        
