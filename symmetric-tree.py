"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).  Problem found here:
http://oj.leetcode.com/problems/symmetric-tree/
"""



# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.checkSymmetry(root.left, root.right)
    
    def checkSymmetry(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return (self.checkSymmetry(left.left, right.right) and
                    self.checkSymmetry(left.right, right.left))

#test
sol = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
print 'expected value wastrue, returned: ', sol.isSymmetric(root)
root.left.val = 2
print 'expected value was false, returned: ', sol.isSymmetric(root)
