class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def help(idx,holding):
            if idx>=n:
                return 0
            if (idx,holding) in memo:
                return memo[(idx,holding)]
            ans1 = 0
            ans2 = 0
            if holding:
                Sell = help(idx+2,False) + prices[idx]
                Leave = help(idx+1,True)
                ans1 = max(Sell,Leave)
                memo[(idx,holding)] = ans1
            else:
                Buy = help(idx+1,True) - prices[idx]
                Leave = help(idx+1,False)
                ans2 = max(Buy,Leave)
                memo[(idx,holding)] = ans2
            return max(ans1,ans2)
            
        return help(0,False)
            
        