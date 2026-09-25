class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)

        for i,val in enumerate(citations):
            if val<i+1:
                return i

        return len(citations)