"""
Given a linked list, return the node where the cycle begins. If there
is no cycle, return null.
Follow up:
Can you solve it without using extra space?
Problem found here:
http://oj.leetcode.com/problems/linked-list-cycle-ii/
"""

import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        count = 20
        string = '['
        cur = self
        while cur:
            if cur.next is None:
                string += str(cur.val) + ']'
            else:
                string += str(cur.val) + ', '
            cur = cur.next
            count -= 1
            if count == 0:
                cur = None
                string += ' string is looping (or is longer than 20 items)'
        return string


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        while True:
            if fast.next is None or fast.next.next is None:
                return None
            else:
                fast = fast.next.next
                slow = slow.next
                if fast is slow:
                    break
        slow = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast


#test
sol = Solution()
no_loop = ListNode(0)
cur = no_loop
for i in range(1,10):
    cur.next = ListNode(i)
    cur = cur.next
big_loop = ListNode(0)
cur = big_loop
for i in range(1,10):
    cur.next = ListNode(i)
    cur = cur.next
cur.next = big_loop
small_loop = ListNode(0)
cur = small_loop
for i in range(1,10):
    cur.next = ListNode(i)
    cur = cur.next
cur.next = cur
random_loop = ListNode(0)
cur = random_loop
loop_point = None
for i in range(1,10):
    cur.next = ListNode(i)
    if random.randint(2,8) == i:
        loop_point = cur
    cur = cur.next
cur.next = loop_point
print 'the first list is:', no_loop
print 'our system finds that the loop happens at: ',
print sol.detectCycle(no_loop), '\n'
print 'the second list is:', big_loop
print 'our system finds that the loop happens at: ',
print sol.detectCycle(big_loop).val, '\n'
print 'the third list is:', small_loop
print 'our system finds that the loop happens at: ',
print sol.detectCycle(small_loop).val, '\n'
print 'the fourth list is:', random_loop
detected_loop = sol.detectCycle(random_loop)
if detected_loop is None:
    print 'our system finds that there is no loop in this list'
else:
    print 'our system finds a loop in this list at node:', detected_loop.val
