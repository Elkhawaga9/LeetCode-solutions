class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        ans = 0
        i = 1
        while i < len(arr) - 1:
            # Check if arr[i] is a peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = right = i

                # Move left
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Move right
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1

                ans = max(ans, right - left + 1)

                # Move to the right of the mountain
                i = right
            else:
                i += 1

        return ans if ans >= 3 else 0


