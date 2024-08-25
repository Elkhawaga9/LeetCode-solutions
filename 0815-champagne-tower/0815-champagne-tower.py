class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(i+1) for i in range(query_row+1)]
        dp[0][0] = poured
        for row in range(query_row):
            for col in range(row+1):
                rest = dp[row][col] - 1
                if rest>0:
                    dp[row+1][col] += rest/2 
                    dp[row+1][col+1] += rest/2 
        print(dp)
        return min(1,dp[query_row][query_glass])

        