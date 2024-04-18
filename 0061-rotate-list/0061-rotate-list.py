# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not k or not head or not head.next:
            return head
        sz = 0
        current = head
        fake = ListNode(0,head)
        while(current):
            sz+=1
            current = current.next
        k%=sz
        if (not k):
            return head
        pre = fake
        left = head
        right = head
        beforeright = fake
        for _ in range(k):
            beforeright = right
            right = right.next
        while (right):
            beforeright = right
            right = right.next
            pre = pre.next
            left = left.next
        """print(pre)
        print(left)
        print(beforeright)"""
        pre.next = None
        beforeright.next = head
        return left


        