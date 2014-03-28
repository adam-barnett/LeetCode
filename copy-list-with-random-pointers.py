"""
A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.
Return a deep copy of the list. Problem from here:
http://oj.leetcode.com/problems/copy-list-with-random-pointer/
note. it appears there is also a requirement that the original not be changed
"""

import random

# Definition for singly-linked list with a random pointer.
# I have altered the class from the version used on Leetcode to allow
# printing for tests.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        string = 'main list - ['
        cur = self
        while cur:
            if cur.next is None:
                string += str(cur.label) + ']'
            else:
                string += str(cur.label) + ', '
            cur = cur.next
        cur = self
        string += '\nrandom pointers - ['
        while cur:
            if cur.next is None:
                if cur.random is None:
                    string += '_]'
                else:
                    string += str(cur.random.label) + ']'
            else:
                if cur.random is None:
                    string += '_, '
                else:
                    string += str(cur.random.label) + ', '
            cur = cur.next
        return string

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return head
        cur = head
        #duplicating the list
        while cur is not None:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        #duplicating the random pointers
        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        #extracting the new list and putting the original back together
        new_head = head.next
        new_cur = head.next
        cur = head
        while new_cur.next is not None:
            cur.next = cur.next.next
            cur = cur.next
            new_cur.next = new_cur.next.next
            new_cur = new_cur.next
        cur.next = None
        return new_head


#test
sol = Solution()
head = RandomListNode(0)
size = 10
cur = head
nodes = []
nodes.append(cur)
for i in range(1,size):
    cur.next = RandomListNode(i)
    cur = cur.next
    nodes.append(cur)
cur = head
while cur is not None:
    cur.random = nodes[random.randint(0,size-1)]
    cur = cur.next
list_copy = sol.copyRandomList(head)
print 'The input list is : ', head
print 'Which should be the same as that returned by our method'
print 'which is: ', list_copy
print 'Also the two methods are not equal: ', list_copy is not head
