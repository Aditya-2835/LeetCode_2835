class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        min_sum=float('inf')
        cur_max=cur_min=0

        for i in nums:
            cur_max=max(i,cur_max+i)
            max_sum=max(cur_max,max_sum)

            cur_min=min(i,cur_min+i)
            min_sum=min(cur_min,min_sum)

        return max(abs(max_sum),abs(min_sum))