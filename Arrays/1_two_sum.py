from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for indx, num in enumerate(nums):
            d[num] = indx

        for indx, num in enumerate(nums):
            search_value = target - num
            if d.get(search_value) and d.get(search_value) != indx:
                return [indx, d.get(search_value)]
        return []