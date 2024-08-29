# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        d = defaultdict(int)
        d[0] = 1
        def dfs(node,currentSum):
            nonlocal ans
            if node==None:
                return
#5 target-c = 5 
            newSum = currentSum+node.val

            d[newSum]+=1
            if newSum-targetSum in d:
                ans+=d[newSum-targetSum]
            dfs(node.left,newSum)
            dfs(node.right,newSum)
            d[newSum]-=1

        dfs(root,0)
        return ans


            

        