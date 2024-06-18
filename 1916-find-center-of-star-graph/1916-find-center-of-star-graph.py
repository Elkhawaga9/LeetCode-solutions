class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        d = [0 for _ in range (n+2)]
        for l,r in edges:
            d[l]+=1
            d[r]+=1
        for i in range(1, n + 2):  
            if d[i] == n:
                return i
        

        