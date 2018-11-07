# -*- coding:utf-8 _*_
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        if n==1:
            return ['()']
        ans=['()']
        for i in range(2,n+1):
            tem=[]
            for j in ans:
                tem1='('+j
                for k in range(len(tem1)):
                    if tem1[k]=='(':
                        tem2=tem1[0:k+1]+')'+tem1[k+1:]
                        tem.append(tem2)
                    else:
                        break
            ans=tem.copy()
        return ans
o=Solution()
print(o.generateParenthesis(3))

