# -*- coding:utf-8 _*_
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        stack1=[]
        stack2=[]
        for i in range(len(s)):

            if s[i]=='(':
                stack2.append(i)
                stack1.append('(')
            else:
                if bool(stack1):
                    if stack1[len(stack1)-1]=='(':
                        stack2.pop()
                        stack1.pop()
                    else:
                        stack1.append(')')
                        stack2.append(i)
                else:
                    stack1.append(')')
                    stack2.append(i)

        if stack1==[]:
            return len(s)
        else:
            t=-1
            stack2.append(len(s))
            for i in stack2:
                ans=max(ans,i-t-1)
                t=i
        return ans
o=Solution()
print(o.longestValidParentheses(""))