class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda:float('inf'))
        def help(rest):
            if rest==0:
                return 0
            elif rest<0:
                return float('inf')
            if rest in memo:
                return memo[rest]
            min_coins = float('inf')
            for i in coins:
                min_coins = min(1+help(rest-i),min_coins)
            memo[rest] = min_coins
            return memo[rest]
        ret = help(amount)
        return ret if ret!=float('inf') else -1