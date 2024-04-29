# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)  
        dummy.next = head  
        prev = dummy
        current = head
        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            if prev.next != current:  
                prev.next = current.next  
            else:
                prev = prev.next  
            current = current.next
        return dummy.next  
