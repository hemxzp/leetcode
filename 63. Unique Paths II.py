# -*- coding:utf-8 _*_
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        a = len(obstacleGrid)
        b = len(obstacleGrid[0])
        ans=[0]*b
        for i in range(b-1,-1,-1):
            if obstacleGrid[-1][i]==0:
                ans[b-1-i]=1
            else:
                break
        for i in range(a - 1):
            for j in range(b):
                if obstacleGrid[a-2-i][b-1-j]==1:
                    ans[j]=0
                else:
                    if j>0:
                        ans[j] += ans[j - 1]
        return ans[b - 1]
o=Solution()
tem=[

  [0],[1]

]
print(o.uniquePathsWithObstacles(tem))