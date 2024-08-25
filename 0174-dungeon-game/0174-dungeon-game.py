class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m = len(dungeon),len(dungeon[0])
        memo = {}
        def dp(i,j):
            if i==n-1 and j==m-1:
                if dungeon[i][j]>=0:
                    return 1
                else:
                    return -dungeon[i][j]+1
            if (i,j) in memo:
                return memo[(i,j)]
            best = 10**10
            #right
            # -2  -3  3
            # 6 <-4 <- 1
            if j+1<m:
                right = dp(i,j+1)
                if dungeon[i][j] < right:
                    best = min(best,right + (-dungeon[i][j]))
                else:
                    best = min(best,1)
                
            #down 3  1  -5
            #     1  4   5
            if i+1<n:
                down = dp(i+1,j)
                if dungeon[i][j] < down:
                    best = min(best,down + (-dungeon[i][j]))
                else:
                    best = min(best,1)
            memo[(i,j)] = best
            return best
        return dp(0,0)






            

        