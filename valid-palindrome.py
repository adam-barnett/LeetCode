"""
Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases. problem found here:
http://oj.leetcode.com/problems/valid-palindrome/
"""



class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        s = s.lower()
        forwards = 0
        backwards = len(s)-1
        mid = int(len(s)/2)
        while forwards != backwards and not forwards > backwards:
            if  not s[forwards].isalnum():
                forwards += 1
            elif  not s[backwards].isalnum():
                backwards -= 1
            elif s[forwards] == s[backwards]:
                forwards += 1
                backwards -= 1
            else:
                return False
        return True


#test
sol = Solution()
example1 = 'ab'
example2 = 'aba'
print 'for example: ', example1
print 'expected false, got: ', sol.isPalindrome(example1)
print 'for example: ', example2
print 'expected true, got: ', sol.isPalindrome(example2)
