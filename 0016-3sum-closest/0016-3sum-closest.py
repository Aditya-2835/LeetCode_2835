class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        res_sum=0

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            while j<k:
                total=nums[i]+nums[j]+nums[k]
                d=abs(target-total)

                if diff>d:
                    diff=d
                    res_sum=total

                if total == target:
                    return res_sum

                elif total<target:
                    j+=1
                else:
                    k-=1
        return res_sum