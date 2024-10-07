# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,1)])
        ans = 1
        while q:
            current_level = []
            for i in range(len(q)):
                current,idx = q.popleft()
                if current.left:
                    q.append((current.left,2*idx))
                if current.right:
                    q.append((current.right,2*idx+1))
                current_level.append(idx)
            ans = max(ans,current_level[-1]-current_level[0]+1)

        return ans
        
        