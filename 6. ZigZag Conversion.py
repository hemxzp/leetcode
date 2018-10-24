# -*- coding:utf-8 _*_
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        re=True
        t=0
        a=[]
        if numRows==1:
            return (s)
        for i in range(numRows):
            a.append([])
        for i in s:
            if re:
                if t<=numRows-1:
                    a[t].append(i)
                    t+=1
                else:
                    t=numRows-2
                    a[t].append(i)
                    re=False
                    t-=1
            else:
                if t>=0:
                    a[t].append(i)
                    t-=1
                else:
                    t=1
                    a[t].append(i)
                    re=True
                    t+=1
        s1=''
        for i in range(numRows):
            s1+=''.join(a[i])
        return(s1)
ob=Solution()
print(ob.convert('PAYPALISHIRING',4))

