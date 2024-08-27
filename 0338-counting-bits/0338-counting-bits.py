class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            for j in range(64):
                if ((1<<j)&i):
                    ans[i]+=1
        #print(ans)    
        return ans