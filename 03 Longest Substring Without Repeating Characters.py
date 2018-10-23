# -*- coding:utf-8 _*_
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=1
        a=[]
        if s=='':
            return (0)
        for i in s:
            if i not in a:
                a.append(i)
            else:
                while a[0]!=i:
                    a.pop(0)
                a.pop(0)
                a.append(i)
            if len(a)>m:
                m=len(a)
        return (m)
ob=Solution()
print(ob.lengthOfLongestSubstring('pwwkew'))
