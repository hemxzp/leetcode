# -*- coding:utf-8 _*_
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        c=0
        if dividend<0:
            dividend=-dividend
            c+=1
        if divisor<0:
            divisor=-divisor
            c+=1
        ans=dividend//divisor
        if c==1:
            ans=-ans
        if ans >pow(2,31)-1 or ans <-pow(2,31):
            return pow(2,31)-1
        else:
            return ans