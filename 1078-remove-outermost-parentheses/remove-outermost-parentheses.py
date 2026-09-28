class Solution(object):
    def removeOuterParentheses(self, s):
        count = 0
        result =""
        for char in s :
            if char == "(":
                count += 1
                if count > 1 :
                    result += char
            if char == ")" :
                count -= 1
                if count > 0 :
                    result += char
        return result
