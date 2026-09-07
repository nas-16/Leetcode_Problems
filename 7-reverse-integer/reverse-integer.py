class Solution(object):
    def reverse(self, x):
        if (x > 0) :
            sign = 1
        else :
            x = x*-1
            sign = -1
        rev = 0
        while(x):
            rem = x%10
            rev = rev*10 + rem
            x = x/10
        if (rev >(2**31)-1 or rev <(-2**31)) :
            return 0
        else :
            return rev*sign
        