from collections import defaultdict
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        n = len(intervals)
        ans = [-1]*(n)
        for i in range (n):
            d[tuple(intervals[i])] = i
# [1,2],[2,3],[3,4] 
# [1,4],[2,3],[3,4]
#  -1, ,  2,   -1

        intervals.sort()
    # 1 3 4 5
        def findLowerBound(item):
            l = 0
            r = n-1
            tmp = -1
            while(l<=r):
                mid = (l+r)//2
                if intervals[mid][0] >=item:
                    tmp = mid
                    r = mid-1 
                else:
                    l = mid + 1
                    
            return tmp 

        for x,y in intervals: 
            z = findLowerBound(y)
            if z != -1:
                ans[d[(x, y)]] = d[tuple(intervals[z])]

        return ans
        



        


