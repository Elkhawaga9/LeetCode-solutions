class Solution(object):
    def hammingWeight(self, n):
        ans=0
        for i in range(33):
            if((1<<i) & n ):
                ans+=1
        return ans  