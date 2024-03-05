from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        ans = []
        d = defaultdict(list)
        m = len(mat)
        n=len(mat[0])

        for i in range(m):
            for j in range(n):
                d[i+j].append(mat[i][j])

        for x,y in d.items():
            if (x%2==0):
                d[x].reverse()
        
        for x,y in d.items():
            ans.extend(y)    
            
        return ans
