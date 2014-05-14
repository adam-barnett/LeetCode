"""
Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.
(it isn't specified in the question, but the lists should be ordered with
the smallest first)
Problem found here:
http://oj.leetcode.com/problems/merge-two-sorted-lists/
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
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        cur = head
        while l1 or l2:
            if l1 is None:
                cur.next = l2
                l2 = None
            elif l2 is None:
                cur.next = l1
                l1 = None
            elif l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                cur.next = None
        return head

#test
sol = Solution()
head1 = None
head2 = None
print 'for two empty lists my solution returns:',
print sol.mergeTwoLists(head1, head2)
head1 = ListNode(0)
cur = head1
for i in xrange(1,10):
    cur.next = ListNode(i)
    cur = cur.next
print 'for one empty and one non empty list containing:', head1,
print 'my solution returns:', sol.mergeTwoLists(head1, head2)
head2 = ListNode(0)
cur = head2
for i in xrange(1,20,2):
    cur.next = ListNode(i)
    cur = cur.next
print 'for two lists containing:', head1, 'and', head2
print 'my solution returns:', sol.mergeTwoLists(head1, head2)
    
