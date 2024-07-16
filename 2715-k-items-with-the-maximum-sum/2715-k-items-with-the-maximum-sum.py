class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = min(numOnes,k)
        if k<=numOnes:
            return ans
        k-=numOnes

        if k <=numZeros:
            return ans
        k-=numZeros

        ans-=min(k,numNegOnes)
        return ans
