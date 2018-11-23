# -*- coding:utf-8 _*_
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a=min(m,n)
        b=max(m,n)
        ans=[1]*b
        for i in range(a-1):
            for j in range(1,b):
                ans[j]+=ans[j-1]
        return ans[b-1]
o=Solution()
print(o.uniquePaths(1,1))