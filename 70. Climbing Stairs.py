# -*- coding:utf-8 _*_
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1
        a=1
        b=1
        for i in range(n-1):
            tem=a+b
            a=b
            b=tem
        return tem
o=Solution()
print(o.climbStairs(4))