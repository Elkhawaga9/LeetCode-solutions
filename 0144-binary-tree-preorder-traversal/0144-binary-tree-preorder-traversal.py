# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(m):
            if m==None:
                return
            ans.append(m.val)
            preorder(m.left)
            preorder(m.right)
        preorder(root)
        return ans