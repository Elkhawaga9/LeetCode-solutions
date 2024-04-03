class Solution:
    def matrixBlockSum(self, matrix: list[list[int]], k: int) -> list[list[int]]:
        n = len(matrix)
        m = len(matrix[0])


        def calc(r1,j1,r2,j2):
            return (matrix[r2][j2]
                   -(matrix[r2][j1-1] if j1>0 else 0)
                   -(matrix[r1-1][j2]if r1>0 else 0)
                   +(matrix[r1-1][j1-1] if r1>0 and j1>0 else 0))

        # add rows
        for i in range(n):
            for j in range(1,m):
                matrix[i][j] += matrix[i][j-1]
        # add columns
        for i in range(1,n):
            for j in range(m):
                matrix[i][j] += matrix[i-1][j]
        ans = []
        for i in range(n):
            tmp=[]
            for j in range(m):
                r1 = max(0,i-k)
                j1 = max(0,j-k)
                r2 = min(i+k,n-1)
                j2 = min(j+k,m-1)
                tmp.append(calc(r1,j1, r2, j2))
            ans.append(tmp)

        return ans

s1 = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(s1.matrixBlockSum(mat,k))
