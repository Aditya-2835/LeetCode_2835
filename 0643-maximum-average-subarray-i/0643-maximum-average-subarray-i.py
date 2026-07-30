class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind_sum=sum(nums[:k])
        max_avg=wind_sum/k

        if len(nums)<k:
            return -1

        for right in range(k,len(nums)):
            wind_sum+=nums[right]-nums[right-k]
            max_avg=max(max_avg,wind_sum/k)

        return max_avg
            