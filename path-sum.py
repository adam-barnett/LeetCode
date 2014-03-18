"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf
path such that adding up all the values along the path equals the given
sum. Problem can be found here:
http://oj.leetcode.com/problems/path-sum/
"""




# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False
        else:
            return (self.hasPathSum(root.left, sum-root.val) or
                    self.hasPathSum(root.right, sum-root.val))

#test
sol = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print 'expected true, returned: ', sol.hasPathSum(t1, 4)
print 'expected false, returned: ', sol.hasPathSum(t1, 1)
