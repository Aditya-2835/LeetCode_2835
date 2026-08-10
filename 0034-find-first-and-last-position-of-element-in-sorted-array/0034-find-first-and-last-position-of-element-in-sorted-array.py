class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(is_First):
            left,right=0,len(nums)-1
            found=-1

            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    found=mid
                    if is_First:
                        right=mid-1
                    else:
                        left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return found

        first=search(is_First=True)
        if first==-1: 
            return [-1,-1]

        last=search(is_First=False)

        return [first,last]