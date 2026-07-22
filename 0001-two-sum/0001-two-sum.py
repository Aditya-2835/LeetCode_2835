class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1={}

        for i,n in enumerate(nums):
            comp=target-n
            if comp in num1:
                return [num1[comp],i]
            num1[n]=i

        return []