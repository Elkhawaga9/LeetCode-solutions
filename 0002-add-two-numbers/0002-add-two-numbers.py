# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = 0
        p1 = l1
        p2 = l2
        head = ListNode(0,None)
        current = head
        pre = None
        while (p1 or p2):
            current.next = ListNode(0,None)
            summ = 0
            if p1:
                summ+=p1.val
            if p2: 
                summ+= p2.val 

            summ += rest 

            if summ >=10:
                summ %=10
                rest = 1
            else: rest=0
            
            current.val = summ
            pre = current
            current = current.next
            if p1:
                p1 = p1.next
            if p2: 
                p2 = p2.next 
        pre.next = None
        if(rest):
            pre.next = ListNode(rest,None)

        """print(current)
        print(pre)
        print(p1)
        print(p2)"""
        
        return head