class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        ans = []
        min_sum = 10000
        for i in range(len(list1)):
            dict1[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in dict1:
                curr_sum = i+dict1[list2[i]]

                if curr_sum<min_sum:
                    ans.clear()
                    min_sum = curr_sum
                    ans.append(list2[i])
                elif curr_sum==min_sum:
                    ans.append(list2[i])
        return ans
