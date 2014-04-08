"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path
could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
Problem found here:
http://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
"""




# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root, num=''):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            try:
                value = int(num + '%d' % root.val)
                return value
            except ValueError:
                print 'error not a number: ', num, ' and ', root.val
        else:
            return (self.sumNumbers(root.left, num + '%d' % root.val) + 
                    self.sumNumbers(root.right, num + '%d' % root.val))


#test
sol = Solution()
root = TreeNode(1)
value = '1'
size = 9
cur = root
for i in xrange(size):
    cur.left = TreeNode(i)
    value = value + '%d' % i
    cur = cur.left
print 'for the value ', value
print 'our method returns a value of: ', sol.sumNumbers(root)
