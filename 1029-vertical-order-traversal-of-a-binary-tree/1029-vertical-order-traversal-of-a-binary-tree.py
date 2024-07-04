from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_dict = defaultdict(list)
        
        if not root:
            return []

        queue = deque([[root, 0, 0]])

        while queue:
            node, col, row = queue.popleft()
            nodes_dict[(col, row)].append(node.val)
            if node.left:
                queue.append([node.left, col - 1, row + 1])
            if node.right:
                queue.append([node.right, col + 1, row + 1])

        # Flatten the dictionary into a list of (x, y, value) tuples
        flattened_list = [(x, y, val) for (x, y), values in nodes_dict.items() for val in values]
        
        # Sort the list by x, then by y, then by value
        sorted_list = sorted(flattened_list, key=lambda item: (item[0], item[1], item[2]))

        print(flattened_list,sorted_list)

        # Group the values by x
        x_dict = defaultdict(list)
        for x, y, value in sorted_list:
            x_dict[x].append(value)
        print(x_dict)
        # Prepare the answer list
        answer = [x_dict[x] for x in sorted(x_dict)]
        
        return answer
