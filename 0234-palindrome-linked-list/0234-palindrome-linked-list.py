# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        #reverse second part
        current = slow
        prev = None
        while(current):
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        
        #now prev point to the second half
        left = head
        right = prev
        while(right):
            if(left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True


        