# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def merge(left_half: List[int], right_half: List[int]) -> List[int]:
            result = []
            left_ptr, right_ptr = 0, 0
            
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr] <= right_half[right_ptr]:
                    result.append(left_half[left_ptr])
                    left_ptr += 1
                else:
                    result.append(right_half[right_ptr])
                    right_ptr += 1

            result.extend(left_half[left_ptr:])
            result.extend(right_half[right_ptr:])
            
            return result
            
        def mergeSort(left,right):
            if left==right:
                return [nums[left]]
            m = (left+right)//2
            leftHalf = mergeSort(left,m)
            rightHalf = mergeSort(m+1,right)
            return merge(leftHalf,rightHalf)
        nums = []
        current = head
        while(current):
            nums.append(current.val)
            current = current.next
        nums2 = mergeSort(0,len(nums)-1)

        head2 = ListNode(nums2[0],None)
        current = head2
        i = 1
        while i<len(nums2):
            current.next = ListNode(nums2[i],None)
            current = current.next
            i+=1
        return head2
        

