class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(n):
            sum=0
            while n>0:
                d=n%10
                n=n//10
                sum+=d*d
            return sum
        

        slow,fast=n,n

        while True:
            slow=sq(slow)
            fast=sq(sq(fast))
            if fast==1: return True
            if slow==fast: return False