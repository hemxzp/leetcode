# -*- coding:utf-8 _*_
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        a=set()

        for line in matrix:
            t=False
            for j in range(len(line)):
                if line[j]==0:
                    a.add(j)
                    t=True
            if t:
                for j in range(len(line)):
                    line[j]=0
        for i in a:
            for j in range (len(matrix)):
                matrix[j][i]=0

o=Solution()
print(o.setZeroes(
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
))