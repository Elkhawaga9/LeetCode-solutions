class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def help(current,idx):
            if current == amount:
                return 1
            if current>amount:
                return 0
            if idx==n:
                return 0
            if (current,idx) in memo:
                return memo[(current,idx)] 
            Without = help(current,idx+1)
            With = help(current+coins[idx],idx)
            ans = With + Without
            memo[(current,idx)] = ans
            return ans
        return help(0,0)
        