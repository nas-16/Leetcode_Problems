class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def generate(curr,open,closed):
            if open == n and closed == n :
                ans.append(curr)
                return 
            #add ( to current
            if open < n :
                generate(curr + "(" , open + 1,closed)
            if closed < open : 
                generate(curr + ")", open ,closed + 1)
        generate("", 0 , 0 )
        return ans     
        