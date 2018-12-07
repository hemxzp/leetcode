# -*- coding:utf-8 _*_
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        try:
            a = float(s)
            return True
        except:
            return False