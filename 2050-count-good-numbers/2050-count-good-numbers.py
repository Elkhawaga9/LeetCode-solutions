class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        ans = (pow(5,n//2,mod)*pow(4,n//2,mod))%mod
        if n&1:
            ans = (ans*5)%mod
        return ans

        