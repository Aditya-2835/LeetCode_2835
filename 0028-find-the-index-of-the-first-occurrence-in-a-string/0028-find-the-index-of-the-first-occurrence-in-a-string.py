class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Alternative 
        #return haystack.find(needle)
        
        n=len(haystack)
        m=len(needle)
        
        for i in range(0,n-m+1):
            if haystack[i:i+m]==needle:
                return i

        return -1