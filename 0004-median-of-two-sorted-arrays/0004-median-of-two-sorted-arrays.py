class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=sorted(nums1+nums2)
        n=len(res)
        if n%2==0:
            mid=n//2
            median=(res[mid-1]+res[mid])/2
            return float(median)
        else:
            mid=n/2
            return res[int(mid)]
        