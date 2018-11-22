# -*- coding:utf-8 _*_
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(n):
            ans.append([0]*n)
        t=1
        for i in range(n//2):
            m=n-2*i-1
            for j in range(m):
                ans[i][i+j]=t
                t+=1
            for j in range(m):
                ans[i+j][n-1-i]=t
                t+=1
            for j in range(m):
                ans[n-1-i][n-1-i-j]=t
                t+=1
            for j in range(m):
                ans[n-1-i-j][i]=t
                t+=1
        if n%2==1:
            ans[n//2][n//2]=n*n
        return ans
o=Solution()
print(o.generateMatrix(0))

