# -*- coding:utf-8 _*_
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            if s[i]==')':
                ans=max(ans,self.check(s[:i+1]))
        return ans


    def check(self,s):
        s=s[::-1]
        count=0
        res=0
        for i in range(len(s)):
            if s[i]==')':
                count+=1
            else:
                count-=1
                if count==0:
                    res=i+1
                if count<0:
                    break
        return res
o=Solution()

print(o.longestValidParentheses('(())()(((((()'))