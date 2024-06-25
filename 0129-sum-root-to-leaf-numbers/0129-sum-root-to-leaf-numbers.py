# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        tmp = []
        def dfs(node):
            nonlocal ans,tmp
            if node==None:
                return
            tmp.append(str(node.val))
            if not node.left and not node.right:
                ans.append(int("".join(tmp)))
            dfs(node.right)
            #tmp.pop()
            #tmp.append(str(node.val))
            dfs(node.left)
            tmp.pop()
        dfs(root)
        return sum(ans)
        