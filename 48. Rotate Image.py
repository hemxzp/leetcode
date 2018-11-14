# -*- coding:utf-8 _*_
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        for i in range((n+1)//2):
            for j in range(n//2+1):
                self.ro(matrix,i,j,n)

    def ro(self,matrix,i,j,n):
        tem=matrix[j][n-i]
        matrix[j][n-i]=matrix[i][j]
        tem2=matrix[n-i][n-j]
        matrix[n-i][n-j]=tem
        tem=matrix[n-j][i]
        matrix[n-j][i]=tem2
        matrix[i][j]=tem

matrix=[
  [1]

]
o=Solution()
print(o.rotate(matrix))