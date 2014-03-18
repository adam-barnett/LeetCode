"""
Given a binary tree, find its minimum depth.  The minimum depth
is the number of nodes along the shortest path from the root
node down to the nearest leaf node.  Problem found here:
http://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
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
    def minDepth(self, root, depth=1):
        if root == None:
            return depth - 1
        if root.left == None and root.right == None:
            return depth
        elif root.left == None:
            return self.minDepth(root.right, depth + 1)
        elif root.right == None:
            return self.minDepth(root.left, depth + 1)
        else:
            return min(self.minDepth(root.left, depth + 1),
                        self.minDepth(root.right, depth + 1))


#test
sol = Solution()
root = TreeNode(0)
current_node = root
n = 5
for i in xrange(n):
    current_node.left = TreeNode(i)
    current_node = current_node.left
print 'expected value: ', n + 1, " returned value: ", sol.minDepth(root)
root.right = TreeNode(1)
print 'expected value: ', 2, " returned value: ", sol.minDepth(root)
