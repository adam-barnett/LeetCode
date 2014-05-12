"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return - [[5,4,11,2],[5,8,4,5]]
"""

import time
import sys


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
There are three solutions here, two iterative and one recursive.  Initially
I submitted the recursive solution but LeetCode failed it as taking too long,
so I put together the first iterative solution (pathSumIter1) and that passed.
To check why this was I tested them offline here and found that the iterative
solution was actually slower.  Further testing showed that the recursive
solution was failing due to Python's maximum recursive depth.  However I wasn't
happy with the iterative solution being so slow, so I optimised it a bit (by
removing the somewhat hacky way of storing the path in a string).
"""
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum, method='iter1'):
        if method == 'recurse':
            paths = []
            self.pathSumRecurse(root, sum, [], paths)
            return paths
        elif method == 'iter2':
            return self.pathSumIter2(root, sum)
        elif method == 'iter1':
            return self.pathSumIter(root, sum)
        else:
            print 'please provide a valid method from iter1, iter2 and recurse'

    def pathSumRecurse(self, root, sum, stack, paths):
        if root is None:
            return
        stack.append(root.val)
        if root.left is None and root.right is None:
            if sum == root.val:
                paths.append(list(stack))
            return
        self.pathSumRecurse(root.left, sum - root.val, stack, paths)
        self.pathSumRecurse(root.right, sum - root.val, stack, paths)
        stack.pop()
        
    def pathSumIter(self, root, sum):
        if root is None:
            return []
        found_so_far = [(root, str(root.val))]
        word_paths = []
        while found_so_far:
            (node, path) = found_so_far.pop()
            if node.left is None and node.right is None:
                if node.val == sum:
                    word_paths.append(path)
            if node.left is not None:
                next_path = path + '*' + str(node.left.val)
                node.left.val += node.val
                found_so_far.append((node.left, next_path))
            if node.right is not None:
                next_path = path + '*' + str(node.right.val)
                node.right.val += node.val
                found_so_far.append((node.right, next_path))
        full_paths = []
        for path in word_paths:
            full_paths.append(self.decode_paths(path.split('*')))
        return full_paths

    def decode_paths(self, path_string):
        path_list = []
        for num in path_string:
            if num[0] == '-':
                path_list.append(-int(num[1:]))
            else:
                path_list.append(int(num))
        return path_list

    def pathSumIter2(self, root, sum):
        if root is None:
            return []
        found_so_far = [(root, root.val, [root.val])]
        paths = []
        while found_so_far:
            (node, so_far, path) = found_so_far.pop()
            if node.left is None and node.right is None:
                if so_far == sum:
                    paths.append(path)
            if node.left is not None:
                found_so_far.append((node.left, node.left.val + so_far,
                                     path + [node.left.val]))
            if node.right is not None:
                found_so_far.append((node.right, node.right.val + so_far,
                                     path + [node.right.val]))
        return paths
        

def setup(n):
    root = TreeNode(1)
    expand = [root]
    while n:
        node = expand.pop()
        node.left = TreeNode(1)
        node.right = TreeNode(1)
        expand.append(node.left)
        expand.append(node.right)
        n -= 1
    return root

#test timings
rec_error = 'maximum recursion depth exceeded'
sol = Solution()
size = 1500
root = setup(size)
sys.setrecursionlimit(size + 10)
rec_time = 0
for i in xrange(1000):
    try:
        start = time.clock()
        sol.pathSum(root, -5, 'recurse')
        rec_time += time.clock() - start
    except RuntimeError as re:
        if re.message == rec_error:
            print 'max recursive depth exceeded'
            print 'depth is currently', sys.getrecursionlimit()
        else:
            print re.message
        break

root = setup(size)
iter1_time = 0
for i in xrange(1000):
    start = time.clock()
    sol.pathSum(root, -5)
    iter1_time += time.clock() - start
    #root = setup(size)

root = setup(size)
iter2_time = 0
for i in xrange(1000):
    start = time.clock()
    sol.pathSum(root, -5, 'iter2')
    iter2_time += time.clock() - start
    #root = setup(size)
    
print 'Time taken for recursive method: ', rec_time/1000
print 'Time taken for first iterative method: ', iter1_time/1000
print 'Time taken for second iterative method: ', iter2_time/1000
