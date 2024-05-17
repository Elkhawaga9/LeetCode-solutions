# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.right and root.left:
            if root.right.val>root.val>root.left.val:
                return self.isValidBST(root.right) and self.isValidBST(root.left)
            else:
                return False
        elif root.right:
            return self.isValidBST(root.right) and root.val<root.right.val
        elif root.left:
            return self.isValidBST(root.left) and root.val>root.left.val
        else:
            return True

        
        