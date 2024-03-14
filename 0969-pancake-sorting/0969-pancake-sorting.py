class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        ans = []
        end = len(arr)

        while end>1:
            print(arr)
            idx = arr.index(end)
            print(idx)
            if idx == end-1:
                end -= 1

            else:
                if idx!=0:
                    ans.append(idx+1)
                    arr[0:idx+1] = reversed(arr[0 : idx+1])
                ans.append(end)
                arr[:end]=reversed(arr[:end])
        return ans