
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_table = dict()

        for num in nums:
            if hash_table.get(num):
                return True
            else:
                hash_table[num] = 1

        return False