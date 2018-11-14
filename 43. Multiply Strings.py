# -*- coding:utf-8 _*_
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0]*(len(num1)+len(num2)+1)
        for i in range(len(num1)):
            for j in  range(len(num2)):
                ans[i+j] += int(num1[i])*int(num2[j])
        t=0
        add=0
        while  t<len(ans)-1:
            add=ans[t]//10
            ans[t]=ans[t]%10
            t+=1
            ans[t]+=add
        while ans[-1]==0:
            ans.pop()
        s=''
        for i in ans:
            s=str(i)+s
        return s
o=Solution()
print(o.multiply('99','99'))