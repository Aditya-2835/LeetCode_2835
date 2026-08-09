class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq={}
        one,zero=0,0
        res=0

        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else: one+=1

            diff=zero-one

            if diff==0:
                res=max(res,i+1)

            if diff not in freq:
                freq[diff]=i
            else:
                idx=freq[diff]
                l=i-idx
                res=max(res,l)

        return res
