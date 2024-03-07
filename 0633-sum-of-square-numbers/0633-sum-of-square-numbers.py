from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int(sqrt(c))+1):
            nd = c - (i * i)
            if nd >=0 and int(sqrt(nd)) * int(sqrt(nd)) == nd:
                return True
        return False

