# -*- coding:utf-8 _*_
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.firstnode=None
        self.secondnode=None
        self.prenode=TreeNode(-1000000000)
        def traverse(root):

            if root==None:
                return
            traverse(root.left)
            if (self.firstnode == None) & (self.prenode.val>root.val):
                self.firstnode=self.prenode
            if (self.firstnode !=None) & (self.prenode.val>root.val):
                self.secondnode=root
            self.prenode=root
            traverse(root.right)
        traverse(root)
        tem=self.firstnode.val
        self.firstnode.val=self.secondnode.val
        self.secondnode.val=tem
a=TreeNode(1)
a.left=TreeNode(3)
a.right=TreeNode(2)
o=Solution()
print(o.recoverTree(a))


