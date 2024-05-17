from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float('-inf'), upper=float('inf')) -> bool:
        if root is None:
            return True
        
        val = root.val
        if val <= lower or val >= upper:
            return False
        
        if not self.isValidBST(root.right, val, upper):
            return False
        if not self.isValidBST(root.left, lower, val):
            return False
        
        return True
