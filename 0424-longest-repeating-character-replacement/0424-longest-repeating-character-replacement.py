class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        freq={}
        res=0

        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1
            l=high-low+1
            maj=max(freq.values())
            diff=l-maj

            while diff>k:
                freq[s[low]]-=1
                low+=1
                l=high-low+1
                maj=max(freq.values())
                diff=l-maj
            
            res=max(res,l)

        return res
