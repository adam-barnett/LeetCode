"""
Given a non-negative number represented as an array of digits, plus one to
the number.
The digits are stored such that the most significant digit is at the head
of the list.
Problem found here:
http://oj.leetcode.com/problems/plus-one/
"""



class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if len(digits) == 0:
            digits.append(1)
            return digits
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        index = len(digits)-2
        digits[-1] = 0
        while index > -1:
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                return digits
        #note. I am prepending to the list here in order that the original
        #list is changed in place. 'return [1] + digits' would work
        #fine if we were instead simply using the return value 
        digits.reverse()
        digits.append(1)
        digits.reverse()
        return digits


#test
sol = Solution()
num = [9]*2 + [8]
print 'initially the number is:', num
print 'after adding one the number is:', sol.plusOne(num)
print 'after adding another one the number is:', sol.plusOne(num)
print 'adding a final one gives:', sol.plusOne(num)
