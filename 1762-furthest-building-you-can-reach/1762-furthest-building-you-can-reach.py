from heapq import *
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        min_heap = []
        ans = 0
        for i in range(1,n):
            diff =heights[i]-heights[i-1]
            if diff > 0:
                if ladders:
                    heappush(min_heap,diff)
                    ladders-=1
                    ans = i
                    continue
                heappush(min_heap,diff)
                if min_heap:
                    z = heappop(min_heap)
                    if z<=bricks:
                        bricks -= z
                        ans = i
                    else:
                        break
                else:
                    if diff<=bricks:
                        bricks -= diff
                        ans = i
                    else:
                        break
            else:
                ans = i
        return ans
