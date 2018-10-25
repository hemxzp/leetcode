# -*- coding:utf-8 _*_
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start=0
        if str=='':
            return (0)

        while start<len(str) and str[start]==' ':
            start+=1

        if start==len(str):

            return (0)
        if not str[start].isdigit():
            if str[start]!='-' and str[start]!='+':
                return (0)
        end=start
        while end+1<len(str) and str[end+1].isdigit():
            end+=1
        str=str[start:end+1]
        if len(str)==1:
            if str=='+' or str=='-':

                return (0)
        if int(str)>pow(2,31)-1 :
            return (pow(2,31)-1)
        if int(str)<-pow(2,31):
            return (-pow(2,31))
        return (int(str))
ob=Solution()
print(ob.myAtoi(' 1'))