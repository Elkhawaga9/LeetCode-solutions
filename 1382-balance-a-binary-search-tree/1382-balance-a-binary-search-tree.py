# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def getNums(node):
            nonlocal nums
            if node==None:
                return
            nums.append(node.val)
            getNums(node.left)
            getNums(node.right)
        getNums(root)
        nums.sort()
        def makeTree(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = makeTree(l,mid-1)
            root.right = makeTree(mid+1,r)
            return root
        return makeTree(0,len(nums)-1)








        
        