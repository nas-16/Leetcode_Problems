class Solution(object):
    def myAtoi(self, s):
        
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Build number
        num = 0

        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num *= sign
        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1
        return num
            

            