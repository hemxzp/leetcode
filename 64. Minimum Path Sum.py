# -*- coding:utf-8 _*_
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=len(grid)
        b=len(grid[0])

        ans=[0]*b
        ans[0]=grid[0][0]
        for i in range(1,b):
            ans[i]=ans[i-1]+grid[0][i]

        for i in range(1,a):
            for j in range(b):
                if j==0:
                    ans[0]=ans[0]+grid[i][j]
                else:
                    ans[j]=min(ans[j],ans[j-1])+grid[i][j]
        return ans[b-1]
tem=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
o=Solution()
print(o.minPathSum(tem))