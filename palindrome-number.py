"""
Determine whether an integer is a palindrome. Do this without extra space.
Problem found here:
http://oj.leetcode.com/problems/palindrome-number/
"""



import math

"""
my initial solution.  This works and satisfies the requirement of using no
extra space, but it uses the math library which isn't available on leetcode
so it wasn't acceptable as a solution.
"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        while x > 0:
            if x/(10**int(math.log10(x))) == x % 10:
                x = ((x - (x/(10**int(math.log10(x))))*
                     10**int(math.log10(x))) / 10)
                while x % 10 == 0 and x != 0:
                    x = x / 10
            else:
                return False
        return True


"""
My second solution, defining my own log10 function so it could be accepted.
Additionally I decided that since I needed them for the log10 function I would
allow local variables elsewhere to improve the readability.
"""
class Solution2:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        while x > 0:
            magnitude = 10**int(self.log10(x))
            first_digit = x/magnitude
            last_digit = x % 10
            if first_digit == last_digit:
                x = (x - (first_digit * magnitude)) / 10
                while x % 10 == 0 and x != 0:
                    x = x / 10
            else:
                return False
        return True

    def log10(self, x):
        val = 10
        power = 0
        while True:
            if x < val:
                return power
            else:
                power += 1
                val = val * 10 

#test
sol = Solution2()
numbers = {123454321 : True,
           1232100 : False,
           1 : True,
           0 : True,
           12 : False,
           -1 : False,
           10011001 : True}
for (num, expected) in numbers.iteritems():
    print 'for number: ', num, ' expected: ', expected,
    print 'returned: ', sol.isPalindrome(num)
