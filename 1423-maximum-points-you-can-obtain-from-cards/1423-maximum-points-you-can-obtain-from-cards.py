class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        prefix = [0] * (n)
        suffix = [0] * (n)
        prefix[0] = cardPoints[0]
        suffix[n-1] = cardPoints[n - 1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + cardPoints[i]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + cardPoints[i]
        ans = max(prefix[k - 1], suffix[n - k])
        fst = 0
        lst = n - k + 1
        while (lst != n):
            ans = max(ans, prefix[fst] + suffix[lst])
            fst += 1
            lst += 1
        return ans