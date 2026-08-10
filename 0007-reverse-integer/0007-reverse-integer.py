class Solution:
    def reverse(self, x: int) -> int:
        n=abs(x)
        rev=0

        while n!=0:
            digit=n%10
            rev=rev*10+digit
            n=n//10
        if x<0:
            rev*=-1

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev