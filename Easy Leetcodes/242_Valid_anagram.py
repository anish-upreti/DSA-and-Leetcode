class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        if s_dict == t_dict:
            return True
        else:
            return False
        
        
        
# Alternate solution using Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        if s_dict == t_dict:
            return True
        else:
            return False
