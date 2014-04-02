"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
(http://en.wikipedia.org/wiki/Reverse_Polish_notation)
Valid operators are +, -, *, /. Each operand may be an integer or another
expression.  Problem found here:
http://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
"""

import operator


#this function is needed because python rounds by flooring any integer division
#whereas leetcode expects you to be rounding towards 0
def mydiv(x, y):
    return int(float(x)/y)
        
conv = {"+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": mydiv}
"""
My second solution which passes correctly
"""
class Solution1:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        nums = []
        while len(tokens) > 0:
            if tokens[0] in conv:
                if len(nums) < 2:
                    return -1
                    #print 'error the ordering of the values is wrong'
                else:
                    first = nums.pop()
                    second = nums.pop()
                    nums.append(conv[tokens[0]](second, first))
                    tokens = tokens[1:len(tokens)]
            else:
                try:
                    nums.append(int(tokens[0]))
                    tokens = tokens[1:len(tokens)]
                except ValueError:
                    return -1
                    #print 'error value entered which wasnt and integer or operator'
        if len(nums) == 0:
            return -1
        return nums[-1]

"""
This is my initial solution.  It is correct but exceeds the maximum recursion
depth for very large problems
"""
class Solution2:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens, nums=[]):
        if len(tokens) == 0:
            if len(nums) == 1:
                return nums.pop()
            elif len(nums) == 0:
                return -1
                #print 'error there are not enough numbers'
            else:
                return -1
                #print 'error there are not enough operators'
        elif tokens[0] in conv:
            if len(nums) < 2:
                return -1
                #print 'error the ordering of the values is wrong'
            else:
                first = nums.pop()
                second = nums.pop()
                nums.append(conv[tokens[0]](second, first))
                return self.evalRPN(tokens[1:len(tokens)], nums)
        else:
            try:
                nums.append(int(tokens[0]))
                return self.evalRPN(tokens[1:len(tokens)], nums)
            except ValueError:
                return -1
                #print 'error value entered which wasnt and integer or operator'

sol1 = Solution1()
sol2 = Solution2()
print 'problem one - expected return value 9, our solution1 returns: ',
print sol1.evalRPN(["2", "1", "+", "3", "*"])
print 'and our solution2 returns: ',
print sol2.evalRPN(["2", "1", "+", "3", "*"])
print 'problem two - expected return value 6, our solution1 returns: ',
print sol1.evalRPN(["4", "13", "5", "/", "+"])
print 'and our solution2 returns: ',
print sol2.evalRPN(["4", "13", "5", "/", "+"])
print 'problem three - expected return value 22, our solution1 returns: ',
print sol1.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print 'and our solution2 returns: ',
print sol2.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print 'problem four - expected return value 165, our solution1 returns: ',
print sol1.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/",
                   "-18","8","*","-86","-","-","16","/","26","-14","-","-",
                   "47","-","101","-","163","*","143","-","0","-","171","+",
                   "120","*","-60","+","156","/","173","/","-24","11","+",
                   "21","/","*","44","*","180","70","-40","-","*","86","132",
                   "-84","+","*","-","38","/","/","21","28","/","+","83","/",
                   "-31","156","-","+","28","/","95","-","120","+","8","*",
                   "90","-","-94","*","-73","/","-62","/","93","*","196","-",
                   "-59","+","187","-","143","/","-79","-89","+","-"])
print 'and our solution2 returns: ',
print sol2.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/",
                   "-18","8","*","-86","-","-","16","/","26","-14","-","-",
                   "47","-","101","-","163","*","143","-","0","-","171","+",
                   "120","*","-60","+","156","/","173","/","-24","11","+",
                   "21","/","*","44","*","180","70","-40","-","*","86","132",
                   "-84","+","*","-","38","/","/","21","28","/","+","83","/",
                   "-31","156","-","+","28","/","95","-","120","+","8","*",
                   "90","-","-94","*","-73","/","-62","/","93","*","196","-",
                   "-59","+","187","-","143","/","-79","-89","+","-"])
