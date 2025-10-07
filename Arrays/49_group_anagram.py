
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     anagram_groups[sorted_word].append(word)
        # return list(anagram_groups.values())

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            anagram_groups[tuple(count)].append(word)
        return list(anagram_groups.values())
