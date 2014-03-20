"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Problem can be found here:
http://oj.leetcode.com/problems/reverse-integer/
"""

import sys

"""
My initial solution,  I specifically tried to avoid using a lot of the Python
list slicing which might have made this a lot easier.
This passes but it ignores a lot of edge cases.  Specifically if reversing
an integer causes an overflow (not a huge problem in Python, but still
important to consider), what to do with the zero in '10' or '100' when
reversing (in actuality Python's int() casting already takes care of this but
it seems good to deal with it myself).
"""
class Solution:
    # @return an integer
    def reverse(self, x):
        rev = ''
        cur = str(x)
        if cur[0] == '-':
            rev = rev + '-'
            cur = cur[1:len(cur)]
        for i in xrange(len(cur)-1, -1, -1):
            rev = rev + cur[i]
        return int(rev)

"""
My second solution, takes care of the special cases mentioned above
"""
class Solution2:
    # @return an integer
    def reverse(self, x):
        rev = ''
        cur = str(x)
        if cur[0] == '-':
            rev = rev + '-'
            cur = cur[1:len(cur)]
        trailing_zeros = True
        for i in xrange(len(cur)-1, -1, -1):
            if not trailing_zeros or cur[i] != '0':
                rev = rev + cur[i]
                trailing_zeros = False
        if self.biggerThanMax(rev):
            print '\n reverse() is returning a long not an int'
        return int(rev)

    def biggerThanMax(self, value_string):
        max_int = str(sys.maxint)
        if len(max_int) < len(value_string):
            return True
        elif len(max_int) > len(value_string):
            return False
        else:
            for index in xrange(len(max_int)):
                if int(max_int[index]) < int(value_string[index]):
                    return True
                elif int(max_int[index]) > int(value_string[index]):
                    return False
        return False


sol1 = Solution()
sol2 = Solution2()
x = 123
y = -100
z = str(sys.maxint + 1)[::-1]
print 'on example: ', x
print 'solution 1 returns: ', sol1.reverse(x)
print 'solution 2 returns: ', sol2.reverse(x)
print 'on example: ', y
print 'solution 1 returns: ', sol1.reverse(y)
print 'solution 2 returns: ', sol2.reverse(y)
print 'on example: ', z
print 'solution 1 returns: ', sol1.reverse(z)
print 'solution 2 returns: ', sol2.reverse(z)
