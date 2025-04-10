class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        n=abs(x)
        while(n>0):
            r=n%10
            rev=rev*10 + r
            n=n//10
        if(x<0):rev=-rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

        