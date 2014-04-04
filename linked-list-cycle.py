"""
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
Problem found here:
http://oj.leetcode.com/problems/linked-list-cycle/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#a helper function for creating linked lists
def createLinked(nodes, cycle):
    head = ListNode(nodes[0])
    cur = head
    for i in xrange(1,len(nodes)):
        cur.next = ListNode(nodes[i])
        cur = cur.next
    if cycle:
        cur.next = head
    return head

#a helper function for printing cyclic lists of a known length
def printList(head, size):
    print '[',
    while head != None:
        print head.val, ',',
        head = head.next
        size -= 1
        if size == 0:
            print ']'
            break

"""
My solution.  It works using the tortoise and hare method which uses extra
space but only minimally (for the variables fast and slow)
"""
class Solution:
    # @param head, a ListNode
    # @return a list node
    def hasCycle(self, head):
        if head == None:
            return False
        elif head.next == None:
            return False
        fast = head.next
        slow = head
        while fast.next is not None:
            if fast is slow:
                return True
            elif fast.next is None or fast.next.next is None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return False

#test
sol = Solution()
is_linked = True
size = 30
nodes = range(30)
linked = createLinked(nodes, True)
print 'the list is: ',
printList(linked, size)
print 'it is', is_linked, 'that this list is linked'
print 'our system finds it', sol.hasCycle(linked), 'that the list is linked'
