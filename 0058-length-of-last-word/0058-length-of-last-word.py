class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        
        s=s.strip()
        i=len(s)-1
        count=0
        while s[i]!=" " and i>=0:
            count+=1
            i-=1

        return count