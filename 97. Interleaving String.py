# -*- coding:utf-8 _*_
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        me={}
        def help(i,j,k):
            if (i, j, k) in me: return me[i, j, k]

            if k == len(s3): return (i == len(s1)) and (j == len(s2))
            if i == len(s1): return s2[j:] == s3[k:]
            if j == len(s2): return s1[i:] == s3[k:]
            ans= ((s1[i]==s3[k]) & (help(i+1,j,k+1)))|((s2[j]==s3[k]) &(help(i,j+1,k+1)))
            me[i,j,k]=ans
            return ans
        return help(0,0,0)

o=Solution()
print(o.isInterleave("aabcc", "dbbca", "aadbbcbcac"))


