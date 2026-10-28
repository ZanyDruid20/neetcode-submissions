class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first_count = {}
        second_count = {}
        for i in range(len(s)):
            first_count[s[i]] = 1 + first_count.get(s[i], 0)
            second_count[t[i]] = 1 + second_count.get(t[i], 0)
        return first_count == second_count