class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        my_deque = deque()
        result = []

        # iterate through the lists
        for i in range(len(nums)):
            while my_deque and my_deque[0] < i - k + 1:
                my_deque.popleft()
            while my_deque and nums[i] > nums[my_deque[-1]]:
                my_deque.pop()
            my_deque.append(i)
            if i >= k - 1:
                result.append(nums[my_deque[0]])
        return result