class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        reds = defaultdict(list)
        for f,t in redEdges:
            reds[f].append(t)
        blues = defaultdict(list)
        for f,t in blueEdges:
            blues[f].append(t)
        q = deque()
        # 1 -> red
        # -1 -> blue
        q.append((0,0,0))
        ans = [-1]*(n)
        while q:
            node,col,steps = q.popleft()
            if ans[node] == -1:
                ans[node] = steps
            steps+=1
            if col != -1: # not blue
                for child in blues[node]:
                    q.append((child,-1,steps))
                    
            if col != 1: # not red
                for child in reds[node]:
                    q.append((child,1,steps))
                    
        return ans


        
        