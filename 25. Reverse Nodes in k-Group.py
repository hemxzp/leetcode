# -*- coding:utf-8 _*_
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        q = head
        while q != None:
            count += 1
            q = q.next
        return self.reverse(head, k, count)

    def reverse(self, head, k, l):

        if head == None:
            return None
        if l < k or k == 1:
            return head

        tem = head
        tem1 = tem.next

        for i in range(k - 1):
            tem2 = tem1.next
            tem1.next = tem
            tem = tem1
            tem1 = tem2
        head.next = self.reverse(tem2, k, l - k)

        return tem