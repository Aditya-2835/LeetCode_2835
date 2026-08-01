class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low=0
        count=0

        for i in nums:
            if i==0: count+=1

            if count>k:
                if nums[low]==0: count-=1
                low+=1

        return len(nums)-low