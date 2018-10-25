# -*- coding:utf-8 _*_
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        if a==a[::-1]:
            return (True)
        else:
            return (False)