from collections import defaultdict


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def ok(mid):
            d = defaultdict(int)
            left = 0
            for i in range(mid):
                d[answerKey[i]] += 1
            if min(d['T'], d['F']) <= k:
                return True

            for right in range(mid, len(answerKey)):
                d[answerKey[right]] += 1
                d[answerKey[left]] -= 1
                if d[answerKey[left]] == 0:
                    del d[answerKey[left]]
                if (min(d['T'], d['F']) <= k):
                    return True
                left += 1
            return False

        ans = 0
        l = 0
        r = len(answerKey)
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

