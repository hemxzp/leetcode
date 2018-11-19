# -*- coding:utf-8 _*_
import copy
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        table=[]
        for i in range(n):
            table.append([False]*n)
        ans=[]
        self.solve(n,table,0,ans)
        an=[]
        for i in ans:
            a=[]
            for j in i:
                aa=''
                for k in j:
                    if k:
                        aa=aa+'Q'
                    else:
                        aa=aa+'.'
                a.append(aa)
            an.append(a)
        return an
    def solve(self,n,table,k,ans):
        for i in range(n):
            table[k][i]=True
            if self.check(table,k,i,n):
                if k==n-1:
                    b=copy.deepcopy(table)

                    ans.append(b)
                else:
                    self.solve(n,table,k+1,ans)
            table[k][i]=False
    def check(self,table,k,l,n):
        for i in range(k):
            t=i+1
            if table[i][l]:
                return False
            if t+l<n :
                if table[k-t][l+t]:
                    return False
            if l-t>=0:
                if table[k-t][l-t]:
                    return False
        return True

o=Solution()
print(o.solveNQueens(4))