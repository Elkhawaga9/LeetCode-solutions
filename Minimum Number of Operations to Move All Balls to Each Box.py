class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l1 = []
        for i in range(len(boxes)):
            ans = 0
            for j in range(len(boxes)):
                if i==j:
                    continue
                if boxes[j]=='1':
                    ans+=(abs(i-j))
            l1.append(ans)
        return l1     
        
        
