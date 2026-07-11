class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize the two pointers and maximum area
        left = 0
        right = len(heights) - 1
        max_area = 0
        # traverse from left to right
        while left < right:
            # use the formula to choose two containers
            curr_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, curr_area)
            # if the bars are lesser or greater than the order move them accordingly
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area