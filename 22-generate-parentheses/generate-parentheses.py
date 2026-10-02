class Solution(object):
    def generate(self,curr,open,closed,n,ans):
            if open == n and closed == n :
                ans.append(curr)
                return 
            #add ( to current string
            if open < n :
                self.generate(curr + "(" , open + 1,closed,n,ans)
            #add ) to current string
            if closed < open : 
                self.generate(curr + ")", open ,closed + 1,n,ans)
    def generateParenthesis(self, n):
        ans = []
        self.generate("", 0 , 0 , n, ans)
        return ans     
        