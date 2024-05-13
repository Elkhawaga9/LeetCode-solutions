class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(mid):
            hours = 0
            for i in range(len(piles)):
                hours+=ceil (piles[i]/mid)
                if hours>h: return False
            return True 
            
        l = 0
        r = 10**10
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            if ok(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
        