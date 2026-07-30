class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res={}

        for i in range(len(numbers)):
            comp=target-numbers[i]
            if comp in res:
                return [res[comp],i+1]
            res[numbers[i]]=i+1