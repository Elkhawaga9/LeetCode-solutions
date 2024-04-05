class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowel(word):
            n = len(word)-1
            if (word[0]=='a' or word[0]=='e' or word[0]=='i' or word[0]=='o' or word[0]=='u'):
                if (word[n]=='a' or word[n]=='e' or word[n]=='i' or word[n]=='o' or word[n]=='u'):
                    return 1
            return 0

        prefix = [0]*(len(words))
        prefix[0] = isVowel(words[0])
        for i in range(1,len(words)):
            prefix[i] = prefix[i-1]+(isVowel(words[i]))
        ans = []
        for l,r in queries:
            if l==0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r]-prefix[l-1])
        return ans


        