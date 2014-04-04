"""
sort a linked list using insertion sort.
problem found here:
http://oj.leetcode.com/problems/insertion-sort-list/
"""

import random

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
My original solution, it is too slow, specifically because it is adding
elements on starting from the beginning of the list which means my worst
case is an already sorted list of the type [1,2,....100000].  solution is
to check against the tail of the sorted list as well as the head.  As
seen below in Solution2
"""
class Solution1:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None:
            return head
        next = head.next
        sorted = head
        sorted.next = None
        while next != None:
            to_insert = next
            next = next.next
            to_insert.next = None
            sorted = self.insert(sorted, to_insert)
        return sorted
        
    def insert(self, sorted, to_insert):
        if to_insert.val <= sorted.val:
            temp = sorted
            to_insert.next = temp
            sorted = to_insert
        else:
            prev = sorted
            next = sorted.next
            while next != None:
                if to_insert.val <= next.val:
                    prev.next  = to_insert
                    to_insert.next = next
                    return sorted
                else:
                    prev = next
                    next = next.next
            prev.next = to_insert
        return sorted
            

    def printLinkedList(self, linked):
        step_through = linked
        while step_through != None:
            print step_through.val
            step_through = step_through.next

"""
My second solution, this is correct and fast enough.
"""
class Solution2:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None:
            return head
        next = head.next
        sorted = head
        sorted.next = None
        tail = head
        while next != None:
            to_insert = next
            next = next.next
            to_insert.next = None
            (sorted, tail) = self.insert(sorted, tail, to_insert)
        return sorted
        
    def insert(self, sorted, tail, to_insert):
        if to_insert.val <= sorted.val:
            temp = sorted
            to_insert.next = temp
            sorted = to_insert
        elif to_insert.val >= tail.val:
            tail.next = to_insert
            tail = to_insert
        else:
            prev = sorted
            next = sorted.next
            while next != None:
                if to_insert.val <= next.val:
                    prev.next  = to_insert
                    to_insert.next = next
                    return sorted, tail
                else:
                    prev = next
                    next = next.next
            prev.next = to_insert
            tail = to_insert
        return sorted, tail

#test
sol = Solution2()
num = 40
value_range = 100
head = ListNode(random.randrange(value_range))
cur = head
for i in xrange(num-1, -1, -1):
    cur.next = ListNode(random.randrange(value_range))
    cur = cur.next

print 'unsorted list is: ', head
print 'after sorting the list is: ', sol.insertionSortList(head)
