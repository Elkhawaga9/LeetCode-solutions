# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(current):
            nonlocal graph
            if not current:
                return 
            if current.left:
                graph[current.val].append (current.left.val)
                graph[current.left.val].append(current.val)
                dfs(current.left)
            if current.right:
                graph[current.val].append(current.right.val)
                graph[current.right.val].append(current.val)
                dfs(current.right)
        dfs(root)
        print(graph)
        
        q = deque()
        q.append([target.val,0])
        visited = set()
        visited.add(target.val)
        ans = []
        while q:
            cur,step = q.popleft()
            if step==k:
                ans.append(cur)
            elif step<k:
                for i in graph[cur]:
                    if i not in visited:
                        visited.add(i)
                        q.append([i,step+1])

        return ans


        