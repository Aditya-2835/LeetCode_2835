class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        clo_sum=sum(nums[:3])

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            j=i+1
            k=len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==target: return total
                elif abs(total-target)<abs(clo_sum-target): clo_sum=total
                if total<target: j+=1
                else: k-=1
        return clo_sum