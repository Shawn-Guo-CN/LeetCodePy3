#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 23:36
# @Author  : Shawn
# @File    : 19RemoveNthNodeFromEndofList.py
# @Classes :


class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        count = 0
        n_forward_node = head
        while count < n:
            count += 1
            n_forward_node = n_forward_node.next

        pre_cur = None
        cur = head
        while n_forward_node is not None:
            pre_cur = cur
            cur = cur.next
            n_forward_node = n_forward_node.next

        if pre_cur is not None:
            pre_cur.next = cur.next
            return head
        else:
            return []
