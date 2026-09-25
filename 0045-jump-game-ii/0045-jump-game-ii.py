class Solution:
    def jump(self, nums: list[int]) -> int:        
        max_reach=0
        count=0
        cur_end=0

        if len(nums)<=1:
            return 0

        for i,val in enumerate(nums):
            max_reach=max(max_reach,i+val)

            if i==cur_end:
                count+=1
                cur_end=max_reach

                if cur_end>=len(nums)-1:
                    break

        return count
