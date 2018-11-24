# -*- coding:utf-8 _*_
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        an=[]
        ans=[]
        tem=''
        for i in path:
            if i=='/':
                if tem!='':
                    an.append(tem)
                    tem=''
                    continue
            else:
                tem+=i
        if tem!='':
            an.append(tem)
        for i in an:
            if i=='..':
                if ans!=[]:
                    ans.pop()

            elif i!='.':
                ans.append(i)
        res=''
        for i in ans:
            res=res+'/'+i
        if res=='':
            res+='/'
        return res
o=Solution()
print(o.simplifyPath(""))
