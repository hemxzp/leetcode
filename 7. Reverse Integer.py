# -*- coding:utf-8 _*_
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=str(x)

        if x==0:
            return (0)
        ismin=False
        if a[0] == '-':
            a=a[1:]
            ismin=True
        a=a[::-1]
        z=0

        for i in a:
            if i=='0':
                z+=1
            else:
                break
        if ismin:
            a='-'+a[z:]
        else:
            a=a[z:]
        a=int(a)
        if a>pow(2,31)-1 or a<-pow(2,31):
            return (0)
        else:

            return (a)
ob=Solution()
print(ob.reverse(0))
