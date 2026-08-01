class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t): return ""

        need={}
        for i in range(len(t)): need[t[i]]=need.get(t[i],0)+1

        have={}
        req_match=len(need)
        found=0

        low=0
        min_len=float('inf')
        start=-1

        for high in range(len(s)):
            have[s[high]]=have.get(s[high],0)+1

            if s[high] in need and have[s[high]]==need[s[high]]:
                found+=1

            while found==req_match:
                cur_len=high-low+1
                if cur_len<min_len:
                    min_len=cur_len
                    start=low
                have[s[low]]-=1

                if s[low] in need and have[s[low]]<need[s[low]]: found-=1

                low+=1
        
        return "" if min_len==float('inf') else s[start:start+min_len]