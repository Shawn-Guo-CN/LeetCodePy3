# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from math import inf

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = t = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val: 
                l1, l2 = l2, l1
            t.next = l1
            t = t.next
            l1 = l1.next
        t.next = l1 or l2
        return h.next


if __name__ == '__main__':
    h1 = ListNode(1)
    n1_1 = ListNode(2)
    n1_2 = ListNode(4)
    h1.next = n1_1
    n1_1.next = n1_2

    h2 = ListNode(1)
    n2_1 = ListNode(3)
    n2_2 = ListNode(4)
    h2.next = n2_1
    n2_1.next = n2_2

    sol = Solution()
    ret = sol.mergeTwoLists(h1, h2)
