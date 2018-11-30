# -*- coding:utf-8 _*_
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        ans=[0]
        for i in range(n):
            add=pow(2,i)
            tem=[]
            for j in range(len(ans)-1,-1,-1):
                tem.append(ans[j]+add)
            ans+=tem
        return ans
o=Solution()
print(o.grayCode(2))