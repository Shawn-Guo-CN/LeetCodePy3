#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 23:36
# @Author  : Shawn
# @File    : 19RemoveNthNodeFromEndofList.py
# @Classes :


class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        n_forward_node = head
        for _ in range(n):
            n_forward_node = n_forward_node.next

        if n_forward_node is None:
            return head.next

        cur = head
        while n_forward_node.next is not None:
            cur = cur.next
            n_forward_node = n_forward_node.next

        if cur and cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        return head
