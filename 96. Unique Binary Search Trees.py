# -*- coding:utf-8 _*_
class Solution:
    res={}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        for i in range(n):
            if n-1-i not in self.res.keys():
                tem1=self.numTrees(n-1-i)
                self.res[n-i-1]=tem1
            else:
                tem1=self.res[n-i-1]
            if i not in self.res.keys():
                tem2=self.numTrees(i)
                self.res[i]=tem2
            else:
                tem2=self.res[i]
            ans=ans+tem1*tem2
        return ans
o=Solution()
print(o.numTrees(3))