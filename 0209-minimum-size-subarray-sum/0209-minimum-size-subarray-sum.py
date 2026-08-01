class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        cur_sum=0
        min_len=float('inf')

        for high in range(len(nums)):
            cur_sum+=nums[high]

            while cur_sum>=target:
                min_len=min(min_len,high-low+1)
                cur_sum-=nums[low]
                low+=1

        return 0 if min_len==float('inf') else min_len