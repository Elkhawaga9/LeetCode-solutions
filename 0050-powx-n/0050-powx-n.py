class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(xx,nn):
            if nn==0:
                return 1
            if nn>0:
                h = solve(x,nn//2)
                if nn&1:
                    return h*h*xx
                else:
                    return h*h
            else:
                h = solve(1/x,-nn//2)
                if nn&1:
                    return h*h*xx
                else:
                    return h*h
        return solve(x,n)
        



           
       


        