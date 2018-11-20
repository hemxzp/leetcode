# -*- coding:utf-8 _*_
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return []
        if len(matrix)==1:
            return matrix[0]
        if len(matrix)==2:
            return matrix[0]+matrix[1][::-1]
        lenrow=len(matrix[0])
        if lenrow==0:
            return []

        ans=matrix[0]
        matrix.pop(0)
        for i in range(len(matrix)-1):
            ans.append(matrix[i].pop())
        ans+=matrix.pop()[::-1]
        if lenrow>1:
            for i in range(len(matrix)-1,-1,-1):
                ans.append(matrix[i].pop(0))
        return ans+self.spiralOrder(matrix)
m=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
o=Solution()
print(o.spiralOrder(m))