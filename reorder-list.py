"""
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
You must do this in-place without altering the nodes' values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
Problem found here:
http://oj.leetcode.com/problems/reorder-list/
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


"""
My first solution, it is correct but failed on time taken. It works by
steppingthrough the first half of the list, at each step searching all
the way to the end of the list for the next item to add
"""
class Solution1:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return None
        current = head
        while current is not None and current.next is not None:
            move = current.next
            prev = current
            while move.next is not None:
                move = move.next
                prev = prev.next
            prev.next = None
            temp = current.next
            current.next = move
            move.next = temp
            current = current.next.next


"""
My second solution, works by finding the second half of the list, reversing
that and then interleaving the two resulting lists.  This solution passes
all tests.
"""
class Solution2:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return None
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1
        halfway = length/2 + length % 2
        pos = 1
        cur = head
        while pos < halfway:
            cur = cur.next
            pos += 1
        rev = self.reverse(cur.next)
        cur.next = None
        cur = head
        while rev is not None:
            temp = cur.next
            cur.next = rev
            rev_temp = rev.next
            rev.next = temp
            rev = rev_temp
            cur = cur.next.next
            
    def reverse(self, head):
        if head is None:
            return head
        rev_head = head
        head = head.next
        rev_head.next = None
        while head is not None:
            temp = head.next
            head.next = rev_head
            rev_head = head
            head = temp
        return rev_head
        
        


#test
sol = Solution2()
head = ListNode(0)
cur = head
for i in xrange(1,10):
    cur.next = ListNode(i)
    cur = cur.next
print 'A list with an even number of elements is', head
sol.reorderList(head)
print 'reordered list is:', head
head = ListNode(0)
cur = head
for i in xrange(1,9):
    cur.next = ListNode(i)
    cur = cur.next
print 'A list with an odd number of elements is', head
sol.reorderList(head)
print 'reordered list is:', head
