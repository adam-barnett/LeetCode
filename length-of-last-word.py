"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space
characters only.
For example,
Given s = "Hello World",
return 5.
Problem found here:
https://oj.leetcode.com/problems/length-of-last-word/
"""




class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        found =-1
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == ' ' and found != -1:
                return found - i
            elif found == -1 and s[i] != ' ':
                found = i
        if found == -1:
            return 0
        else:
            return found + 1

#test
sol = Solution()
problems = ['word', ' word ', 'word    ', '    word', 'return the final word']
for word in problems:
    print 'for the string:', word
    print 'my system returns the word length:', sol.lengthOfLastWord(word)
    
