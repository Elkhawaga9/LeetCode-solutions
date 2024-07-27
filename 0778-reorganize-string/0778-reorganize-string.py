from collections import Counter
from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        ans = []
        maxHeap = []

        for ch, fr in freq.items():
            heappush(maxHeap, (-fr, ch))

        while maxHeap:
            fr, ch = heappop(maxHeap)
            if not ans or ch != ans[-1]:
                ans.append(ch)
                if -fr != 1:
                    heappush(maxHeap, (fr + 1, ch))
            else:
                if not maxHeap:
                    return ""
                fr2, ch2 = heappop(maxHeap)
                ans.append(ch2)
                if -fr2 != 1:
                    heappush(maxHeap, (fr2 + 1, ch2))
                heappush(maxHeap, (fr, ch))

        return "".join(ans)