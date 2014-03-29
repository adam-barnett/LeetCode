"""
Given a linked list and a value x, partition it such that all nodes less
than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of
the two partitions.
For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
Problem found here:
http://oj.leetcode.com/problems/partition-list/
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
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None:
            return head
        if head.next is None:
            return head
        small_head = None
        small_tail = None
        big_head = None
        big_tail = None
        cur = head
        while cur is not None:
            if cur.val < x:
                if small_head is None:
                    small_head = cur
                    cur = cur.next
                    small_head.next = None
                    small_tail = small_head
                else:
                    small_tail.next = cur
                    cur = cur.next
                    small_tail = small_tail.next
                    small_tail.next = None
            else:
                if big_head is None:
                    big_head = cur
                    cur = cur.next
                    big_head.next = None
                    big_tail = big_head
                else:
                    big_tail.next = cur
                    cur = cur.next
                    big_tail = big_tail.next
                    big_tail.next = None
        if small_head is not None:
            small_tail.next = big_head
            return small_head
        else:
            return big_head

#test
sol = Solution()
head = ListNode(1)
cur = head
size = 5
for i in xrange(5*2, -1, -1):
    cur.next = ListNode(i)
    cur = cur.next
print 'The list passed is: ', head
print 'we are partitioning it based on the number: ', size
print 'which returns: ', sol.partition(head, size)
    
