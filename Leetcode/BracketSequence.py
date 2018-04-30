class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        definitions = {'(':')','[':']','{':'}'}
        size = 0
        stack = []
        for element in s:
            if element == '[' or element == "(" or element == "{":
                stack.append(element)
                size += 1
            elif element == "]" or element == ")" or element == "}":
                if stack:
                    if definitions[stack[size - 1]] == element:
                        size -= 1
                        stack.pop()
                    else:
                        return False
                else:
                    return  False
        return True


sol = Solution()
print(sol.isValid("()"))