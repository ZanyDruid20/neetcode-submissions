class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check if the length of s is less than length of t
        if len(s) < len(t):
            return ""
        # frequencies of characters we need
        target = {}
        # frequencies of characters we have
        window = {}
        # initialize the left pointer
        left = 0
        # builf th the frequency map for t
        for c in t:
            target[c] = target.get(c, 0) + 1
        # then initialize the variable to check the validity of the window
        need = len(target)
        have = 0
        min_length = float("inf")
        result = [-1, -1]   # start and end indices
        # iterate through s while maintaining the window
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0) + 1
            if char in target and window[char] == target[char]:
                have += 1
            while have == need:
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    result = [left, right]
                char = s[left]
                window[char] -= 1
                if char in target and window[char] < target[char]:
                    have -= 1
                left += 1
        if result == [-1, -1]:
            return ""
        start, end = result
        return s[start:end + 1]


            
        