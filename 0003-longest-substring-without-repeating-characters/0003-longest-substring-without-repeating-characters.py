class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        freq={}
        res=0

        for high,val in enumerate(s):
            if val in freq and freq[val]>=low:
                low=freq[val]+1
            freq[val]=high

            res=max(res,high-low+1)

        return res

            