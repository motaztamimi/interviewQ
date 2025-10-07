class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Approach 1: Hash Table
        if len(s) != len(t):
            return False

        table_s = dict()
        
        for char in s:
            table_s[char] = table_s.get(char,0) + 1
        

        table_t = dict()
        
        for char in t:
            table_t[char] = table_t.get(char,0) + 1

        for key, value in table_s.items():
            if not table_t.get(key):
                return False
            if table_t.get(key) != value:
                return False
        return True

        # Approach 2: counter
        counter = [0]*26

        for char in s:
            index = ord(char) - ord('a')
            counter[index]+=1
        for char in t:
            index = ord(char) - ord('a')
            counter[index]-=1
        
        return all(num ==0 for num in counter)