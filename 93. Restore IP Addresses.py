# -*- coding:utf-8 _*_
class Solution:
    ans=[]
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.ans=[]
        self.restore(s,4,[])
        res=[]
        for i in self.ans:
            res.append('.'.join(i))
        return res
    def restore(self,s,t,stack):
        if s=='':
            return
        if t==1:
            if s[0]=='0' and len(s)>1:
                return
            if int(s)<=255:
                stack+=[s]
                self.ans.append(stack.copy())
                stack.pop()
                return
            else:
                return

        if len(s)<t or len(s)>t*3:
            return
        if len(s)>=3:
            if s[0]!='0':
                stack.append(s[0])
                self.restore(s[1:],t-1,stack)
                stack.pop()
                stack.append(s[:2])
                self.restore(s[2:],t-1,stack)
                stack.pop()
                if int(s[:3])<256:
                    stack.append(s[:3])
                    self.restore(s[3:],t-1,stack)
                    stack.pop()
                else:
                    return
            else:
                stack.append('0')
                self.restore(s[1:],t-1,stack)
                stack.pop()
        if len(s)==2:
            stack+=[s[0],s[1]]
            self.ans.append(stack.copy())
            stack.pop()
            stack.pop()
o=Solution()
print(o.restoreIpAddresses("0000"))