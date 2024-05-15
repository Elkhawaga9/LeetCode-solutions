# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        depth = 0
        ans = root.val
        def solve(node,current,fromm):
            nonlocal depth
            nonlocal ans
            if node==None:
                if current > depth:
                    ans = fromm
                    depth = current
                return
            solve(node.left,current+1,node.val)
            solve(node.right,current+1,node.val)
        solve(root,0,root.val)
        return ans