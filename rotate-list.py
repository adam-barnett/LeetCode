"""
Given a list, rotate the list to the right by k places,
where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
problem can be found here:
http://oj.leetcode.com/problems/rotate-list/
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        string = '['
        cur = self
        while cur:
            if cur.next is None:
                string += str(cur.val) + ']'
            else:
                string += str(cur.val) + ', '
            cur = cur.next
        return string
            
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        size = 0
        cur = head
        while cur is not None:
            cur = cur.next
            size += 1
        if size == 0 or head.next is None:
            return head
        k = k % size
        if k == 0:
            return head
        if size == k or k == 0 or size == 0 or head.next is None:
            return head
        elif size < k:
            k = k % size
        back = head
        cur = head
        front = None
        steps = size - k
        while cur.next is not None:
            steps -= 1
            if steps == 0:
                front = cur.next
                cur.next = None
                cur = front
            else:
                cur = cur.next
        cur.next = back
        return front

#test
sol = Solution()
head = ListNode(1)
size = 4
cur = head
for i in xrange(4):
    cur.next = ListNode(i)
    cur = cur.next
rotate = 3
print 'rotating list: ', head, ' by: ', rotate
out = sol.rotateRight(head, rotate)
print 'answer returned is: ', out
