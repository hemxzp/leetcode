# -*- coding:utf-8 _*_
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ans=''
        add=0
        m=max(len(a),len(b))
        t=min(len(a),len(b))
        if len(a)>len(b):
            b='0'*(m-t)+b
        else:
            a='0'*(m-t)+a
        for i in range(1,m+1):
            tem=add+int(a[-i])+int(b[-i])
            add=tem//2
            ans=str(tem%2)+ans
        if add==1:
            ans='1'+ans
        return ans
o=Solution()
print(o.addBinary('11','1'))