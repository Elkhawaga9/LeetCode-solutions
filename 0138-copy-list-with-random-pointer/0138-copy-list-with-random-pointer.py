"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ToCopy = {None:None}
        cur = head
        while(cur):
            tmp = Node(cur.val)
            ToCopy[cur] = tmp
            cur = cur.next
        cur = head
        while cur:
            copy = ToCopy[cur]
            copy.next = ToCopy[cur.next]
            copy.random = ToCopy[cur.random]
            cur = cur.next
        return ToCopy[head]           
        