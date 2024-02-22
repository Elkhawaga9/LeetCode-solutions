class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ans = []
        for i in range(len(matrix[0])):
            t = []
            for l in matrix:
                t.append(l[i])
            ans.append(t)
        return ans
