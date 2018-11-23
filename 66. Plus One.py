# -*- coding:utf-8 _*_
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans=0
        lendigits=len(digits)
        for i in range(len(digits)):
            ans+=digits[lendigits-1-i]*pow(10,i)
        tem=[]
        ans+=1
        while ans>0:
            tem=[ans%10]+tem

            ans=ans//10
        return tem
o=Solution()
print(o.plusOne( [1,2,3]))