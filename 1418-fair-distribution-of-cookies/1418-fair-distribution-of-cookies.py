class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = 9999999
        arr = [0 for _ in range (k)]
        def backtrack(idx):
            nonlocal ans
            if idx==len(cookies):
                ans = min(ans,max(arr))
                return
            if max(arr)>=ans:
                return
            for i in range(k):
                arr[i]+=cookies[idx]
                backtrack(idx+1)
                arr[i]-=cookies[idx]

        backtrack(0)
        return ans
            

        