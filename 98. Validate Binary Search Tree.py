# -*- coding:utf-8 _*_
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a,b,c=self.find(root)
        return a
    def find(self,root):
        if root==None:
            return True,None,None
        l=True
        r=True
        tem1=root.val
        tem2=root.val
        if root.left!=None:
            l,tem1,b=self.find(root.left)
            if not l:
                return False,None,None
            if b>=root.val:
                return False,None,None

        if root.right!=None:
            r,a,tem2=self.find(root.right)
            if not r :
                return False,None,None
            if a<=root.val:
                return False,None,None
        return l & r,tem1,tem2

a=TreeNode(3)

a.right=TreeNode(3)
#a.right.left=TreeNode(10)
#a.right.left.right=TreeNode(15)
#a.right.left.right.right=TreeNode(45)
o=Solution()
print(o.isValidBST(a))