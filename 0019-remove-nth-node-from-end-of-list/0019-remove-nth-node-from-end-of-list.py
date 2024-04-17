# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake = ListNode(0,head)
        beforeMe = fake
        right = fake
        beforeMe = fake
        for i in range(n+1):
            right = right.next
        
        while (right):
            right = right.next
            beforeMe = beforeMe.next
        #print(beforeMe)
        beforeMe.next = beforeMe.next.next
        return fake.next
        
        
        