class Solution(object):
    def isValid(self, s):
        result = []
        for char in s :
            if char in "({[":
                result.append(char)
            else:
                if not result  :
                    return False
                if char == ")" and result[-1] != "(" :
                    return False
                if char == "]" and result[-1] != "[" :
                    return False
                if char == "}" and result[-1] != "{" :
                    return False
                result.pop()
        return not result