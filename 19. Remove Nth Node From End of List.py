# -*- coding:utf-8 _*_
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ans=head
        dic=[head]
        if head==None :
            return None

        while head.next!= None:
            head=head.next
            dic.append(head)
        if len(dic)==1 and n ==1:
            return None

        if len(dic)==n:
            return ans.next
        if n==1:
            dic[len(dic)-2].next=None
            return ans
        dic[len(dic)-n-1].next=dic[len(dic)-n+1]
        return ans
o=Solution()
print(Solution.removeNthFromEnd(ListNode(1),1))
