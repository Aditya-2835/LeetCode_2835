class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1,nums2):
            i=j=0
            res=[]
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    res.append(nums1[i])
                    i+=1
                else:
                    res.append(nums2[j])
                    j+=1

            res.extend(nums1[i:])
            res.extend(nums2[j:])

            return res

        res=merge(nums1,nums2)

        n=len(res)

        if n%2==1:
            return float(res[n//2])
        else:
            return (res[n//2-1]+res[n//2])/2.0