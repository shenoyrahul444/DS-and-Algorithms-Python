class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "" or s == None:
            return True

        string_array = []
        for char in s:
            if char.isalnum():
                if char.isalpha():
                    string_array.append(char.lower())
                elif char.isdigit():
                    string_array.append(char)
        for i in range(len(string_array) // 2):
            if string_array[i] != string_array[len(string_array) - 1 - i]:
                return False

        return True



string = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(string))