# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fake = ListNode(-1,head)
 
        current = head
        pre = fake
        while(current):
            current = pre.next
            if pre.val != current.val:
                pre = pre.next
                current = current.next
            else:
                pre.next = current.next
                current = current.next
        return fake.next

               
        return head



        