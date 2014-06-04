"""
Given a binary tree
struct TreeLinkNode {
    TreeLinkNode *left;
    TreeLinkNode *right;
    TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Note:
    You may only use constant extra space.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
Problem found here:
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/

ALSO:

Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous
solution still work?
Note:
You may only use constant extra space.
For example,
Given the following binary tree,
        1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Problem found here:
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""






# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

        
"""
Solution works for both next right pointers problem and next right pointers ii
"""
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        current = root
        left_most = None
        to_link = None
        while current:
            if current.left:
                if not left_most:
                    left_most = current.left
                if to_link:
                    to_link.next = current.left
                to_link = current.left
            if current.right:
                if not left_most:
                    left_most = current.right
                if to_link:
                    to_link.next = current.right
                to_link = current.right
            if current.next:
                current = current.next
            else:
                current = left_most
                left_most = None
                to_link = None

#test
sol = Solution()
count = 1
root = TreeNode(count)
tree_list = [root]
count += 1
while count < 16:
    fresh_list = []
    for node in tree_list:
        node.left = TreeNode(count)
        count += 1
        node.right = TreeNode(count)
        count += 1
        fresh_list.append(node.left)
        fresh_list.append(node.right)
    tree_list = fresh_list
left_most = tree_list[0]
right_most = tree_list[-1]
sol.connect(root)
print 'the connections found by our system show the bottom',
print 'row of the tree as:'
cur = left_most
while cur:
    print cur.val, '->',
    cur = cur.next
print 'None'
tree_list = [root]
while tree_list:
    fresh_list = []
    for node in tree_list:
        node.next = None
        if node.left:
            if node.left.val < 15 and node.left.val > 8:
                node.left = None
            else:
                fresh_list.append(node.left)
        if node.right:
            if node.right.val < 15 and node.right.val > 8:
                node.right = None
            else:
                fresh_list.append(node.right)
    tree_list = fresh_list
sol.connect(root)
print 'after removing the centre (from 9-14) of the bottom row the',
print 'connections now found by our system are:'
cur = left_most
while cur:
    print cur.val, '->',
    cur = cur.next
print 'None'
