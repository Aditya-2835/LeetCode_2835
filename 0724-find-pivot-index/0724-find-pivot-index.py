class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0

        for i,n in enumerate(nums):
            right=total-left-n
            
            if left==right:
                return i
            
            left+=n

        return -1