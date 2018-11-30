# -*- coding:utf-8 _*_
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        lenmatrix=len(matrix)
        lenline=len(matrix[0])
        res=[]
        t=0
        ans=0
        for i in range (lenline):
            if matrix[0][i]=='0':
                res.append([[0,0]])
                t=0
            else:
                t+=1
                ans=max(ans,t)
                res.append([[t,1]])
        for i in range(1,lenmatrix):
            if matrix[i][0]=='0':
                res[0]=[[0,0]]
            else:
                res[0][0][0]=1
                res[0][0][1]+=1
                ans=max(ans,res[0][0][1])
            for j in range(1,lenline):
                if matrix[i][j]=='0':
                    res[j]=[[0,0]]
                else:
                    tem=res[j][0][1]+1
                    ans=max(ans,tem)
                    res[j]=[[1,tem]]
                    if matrix[i][j-1]=='1':
                        for k in res[j-1]:
                            if k[1]<tem:
                                res[j].append([k[0]+1,k[1]])
                                ans=max(ans,(k[0]+1)*k[1])
                            else:
                                res[j][0]=[k[0]+1,tem]
                                ans=max(ans,(k[0]+1)*tem)
                        if len(res[j])>1:
                            if tem==res[j][1][1]:
                                res[j].pop(0)
        return ans
o=Solution()
print(o.maximalRectangle(

[["0","0","0"],["0","0","0"],["1","1","1"]]))