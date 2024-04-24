from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f_h = defaultdict(int)
        for i in range(len(nums1)):
            f_h[nums1[i]] = i
        stack = []
        ans = [-1]*len(nums1)
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr>stack[-1]:
                val = stack.pop()
                idx = f_h[val]
                ans[idx] = curr
            if curr in f_h:
                stack.append(curr)
        return ans

        