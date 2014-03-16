"""
Given a binary tree, find its maximum depth.
Leetcode problem can be found here:
http://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
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
    def maxDepth(self, root, depth=0):
        if root == None:
            return depth
        elif root.right == None and root.left == None:
            depth += 1
            return depth
        else:
            depth += 1
            return self.bigger(self.maxDepth(root.right, depth),
                                self.maxDepth(root.left, depth))
        
    def bigger(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2

#testing
sol = Solution()
root = TreeNode(0)
current_node = root
n = 5
for i in xrange(n):
    current_node.left = TreeNode(i)
    current_node = current_node.left
print 'expected value was: ', n + 1
print 'found value was: ', sol.maxDepth(root)
    
