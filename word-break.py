"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code". 
Problem found here:
http://oj.leetcode.com/problems/word-break/
"""



"""
Initial recursive solution.  This is correct but takes too long
"""
class Solution1:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) <= 1:
            if s in dict:
                return True
            else:
                return False
        for i in xrange(1,len(s)):
            if s[0:i] in dict:
                if self.wordBreak(s[i::], dict):
                    return True
        return False

"""
A dynamic programming solution which is much faster.  reached is a list
of booleans where the value at index i indicates whether a solution of
valid words has been found to reach the string index s[i-1]
"""
class Solution2:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        length = len(s)
        values = [True] + [False]*length
        for i in xrange(length+1):
            for j in xrange(i):
                if s[j:i] in dict and  values[j] == True:
                    values[i] = True
        return values[-1]
            

#test
sol = Solution2()
words = ['aa']
target = 'aaaaaaaaaaa'#an odd number of 'a's
print 'expecting false, returned', sol.wordBreak(target, words)
words.append('aaa')
print 'expecting true, returned', sol.wordBreak(target, words)
