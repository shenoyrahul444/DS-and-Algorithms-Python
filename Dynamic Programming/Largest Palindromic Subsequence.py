"""
Given a string, find the largest palindromic Subsequence
Example:
 Given a string "ABCBAABCBT"
 Largest Palindomic subsequence for the string would be: "BCBAABCB"
"""

"""Solutions
1> First way is find all the subsequences in the string, Both O(n2) for time and space complexiety . Then for each subsequence check if it is a palindrome, [O(s1)+ O(s2) + O(s3)......(sn)].
    This is a very computationally expensive task with a lot of spaace requirement.
    
2> We can use dynamic programming to solve this problem in O(n2) Time and Space complexiety.
"""

class Solution:
    def getLongestPalindromicString(self,s):
        if s == None:
            return -1
        n = len(s)
        if n== 1:
            return s

        if n == 2 :
            if s[0] == s[1]:
                return s
            else:
                return -1

        table = [[0 for i in range(n)] for j in range(n)]

        maxlength = 1
        i = 0
        while i < n:
            table[i][i] = True
            i +=1
        print(table)


        """ For finding 2 letter words that are same"""
        start = 0
        i=0
        while i < n -2:
            if s[i] == s[i +1 ]:
                table[i][i+1] = True
                maxlength = 2
                start = i
            i += 1

        """ For sequences greater than length 3"""
        k = 3
        while k <= n:
            i = 0
            while i < n - k + 1:
                j = i + k - 1

                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True

                    if k > maxlength:
                        maxlength = k
                        start = i
                i+=1
            k+=1

        print("Maxlength",maxlength)
        print("Start",start)
        # end_index = start + maxlength - 1
        print(start + maxlength - 1)
        print("Largest Palindromic Subsequence : "+ s[start:start + maxlength])

sol = Solution()
sol.getLongestPalindromicString("ACCBAT")

