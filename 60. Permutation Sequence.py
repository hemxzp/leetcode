# -*- coding:utf-8 _*_
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k-=1
        dic=[]
        for i in range(1,n+1):
            dic.append(str(i))
        ans=''
        for i in range(n):
            d=self.mu(n-1-i)
            tem=k//d
            ans+=dic.pop(tem)
            k=k%d
        return ans
    def mu(self,k):
        if k==0:
            return 1
        ans=1
        for i in range(1,k+1):
            ans*=i
        return ans
o=Solution()
print(o.getPermutation(1,1))