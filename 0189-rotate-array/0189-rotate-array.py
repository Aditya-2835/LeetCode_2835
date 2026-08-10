class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums:
            return nums

        k=k%len(nums)

        nums[:]=nums[-k:]+nums[:-k]

        return nums