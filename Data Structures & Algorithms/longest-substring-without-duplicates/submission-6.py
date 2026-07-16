class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need a set to check if the substrings has repeating characters
        seen = set()
        # then we need left pointer and total length to keep track and find the maximum
        left = 0
        total = 0
        # we then use the right pointer to traverse the array
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            total = max(total, right - left + 1)
        return total

