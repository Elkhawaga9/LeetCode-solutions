# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findSmallestInRightSubtree(self, root: TreeNode) -> TreeNode:
        current = root.right
        while current.left is not None:
            current = current.left
        return current
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        if root.val>key:
            root.left = self.deleteNode(root.left, key)
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.val==key and root.right==None:
                return root.left
            elif root.val==key and root.left==None:
                return root.right
            else:
                #find smallest in the right subtree
                smallest = self.findSmallestInRightSubtree(root)
                root.val = smallest.val
                root.right = self.deleteNode(root.right,root.val)
        return root


        