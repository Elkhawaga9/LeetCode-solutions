class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        current = target
        ans = 0
        while(current > 1):
            if not maxDoubles:
                break
            if current%2==0:
                current//=2
                maxDoubles-=1
            else:
                current-=1
            ans+=1
        if current!=1:
            ans += current-1
        return ans
        
        




        