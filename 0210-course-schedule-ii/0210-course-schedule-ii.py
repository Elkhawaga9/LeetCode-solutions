class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque([])
        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for afterthis in graph[node]:
                indegree[afterthis]-=1
                if indegree[afterthis]==0:
                    q.append(afterthis)
        return [] if len(ans)<numCourses else ans
            
