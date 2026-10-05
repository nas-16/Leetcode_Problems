class Solution(object):
    def pow(self,base,exp):
        ans = 1
        mod = (10**9 + 7)
        while exp : 
            if exp % 2 != 0 :
                ans *= base % mod
            base *= base % mod
            exp = exp//2
        return ans

    def countGoodNumbers(self, n):

        even = (n+1)//2
        odd = n//2
        even_ways = self.pow(5,even)
        odd_ways = self.pow(4,odd)

        return (even_ways*odd_ways)%(10**9 + 7)
        