class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = -1, -1

        max_seen = float('-inf')
        min_seen = float('inf')

        for i in range(len(nums)):
            if nums[i] < max_seen:
                end = i
            else:
                max_seen = nums[i]
                
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > min_seen:
                start = i
            else:
                min_seen = nums[i]

        return 0 if end == -1 else end - start + 1