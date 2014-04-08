"""
Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the".
Problem found here
http://oj.leetcode.com/problems/reverse-words-in-a-string/
"""

import re

"""
My original solution where I forced myself to avoid using regex
"""
class Solution1:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        output = ''
        cur = -1
        for i in xrange(len(s)-1, -1, -1):
            if i == 0:
                if cur != -1:
                    if cur - i == 1:
                        output = output + s[cur]
                    else:
                        output = output + s[i:cur+1]
                elif s[i] != ' ':
                    output = output + s[i]
            elif s[i] == ' ' and cur != -1:
                output = output + s[i+1:cur+1] + ' '
                cur = -1
            elif cur == -1 and s[i] != ' ':
                cur = i
            
        return output.strip()

"""
A solution using regular expressions
"""
class Solution2:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = re.findall("([^\s]+)", s)
        words.reverse()
        return " ".join(words)

#Test
sol1 = Solution1()
sol2 = Solution2()
words = ["  and   but  ", " a", "a    removing inner spaces",
         "now sense makes this", "word soup"]
for word in words:
    print 'the results of reversing the sentence: ', word
    print 'with my first solution is: ', sol1.reverseWords(word)
    print 'and with my second solution is: ', sol2.reverseWords(word)


