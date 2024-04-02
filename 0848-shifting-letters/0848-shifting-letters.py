class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        allSum = sum(shifts)
        ans = ""
        for i in range(len(s)):
            ans+=chr(((ord(s[i]) - ord('a') + allSum) % 26) + ord('a'))
            allSum -= shifts[i]
            #print(allSum)

        return ans