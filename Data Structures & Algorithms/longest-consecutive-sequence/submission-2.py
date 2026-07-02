class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        longest = 0
        for n in sequence:
            if (n - 1) not in sequence:
                length = 0
                while (n + length) in sequence:
                    length += 1
                longest = max(length, longest)
        return longest