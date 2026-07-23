class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_index = min(range(len(nums)), key=nums.__getitem__)
        return nums[min_index]