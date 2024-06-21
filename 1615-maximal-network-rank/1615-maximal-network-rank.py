from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        for i in range(len(graph)):
            for j in range(i+1, len(graph)):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    rank -= 1
                ans = max(ans, rank)
        return ans