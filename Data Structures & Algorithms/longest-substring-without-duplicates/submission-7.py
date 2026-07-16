class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we initialize the set
        seen = set()
        # initialize the left pointer, and max number of substrins
        left = 0
        total = 0
        # use right pointer to traverse through the array, and then slide the window 
        # until you see a character without duplicates
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            total = max(total, right - left + 1)
        return total