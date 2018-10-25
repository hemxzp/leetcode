# -*- coding:utf-8 _*_
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pp=p.split('*')
        if p=='' :
            if s=='':
                return True
            else:
                return False

        if len(pp)==1:
            if self.match(s,p):
                return True
            else:
                return False
        if len(pp[0])>1:
            if  not self.match(s[0:len(pp[0])-1],pp[0][:len(pp[0])-1]):
                return (False)
            else:
                s=s[len(pp[0])-1:]
                pp[0]=pp[0][-1]
        p='*'.join(pp[1:])
        if self.isMatch(s,p):
            return True
        else:
            if pp[0]!='.':
                for i in range(len(s)):
                    if s[i]==pp[0]:
                        if self.isMatch(s[i+1:],p):
                            return True
                    else:
                        break
            else:
                for i in range(len(s)):
                    if self.isMatch(s[i+1:],p):
                        return True
        return False


    def match(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i] and s2[i] != '.':
                return (False)
        return (True)

    def find(self,s1,s2):
        for i in range(len(s1)-len(s2)+1):
            t=0
            for j in range(len(s2)):
                if s1[i+j]!=s2[j] and s2[j] != '.':
                    t=1
                    break
            if t==0:
                return i
        return (False)
'''
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

'''
ob=Solution()
print(ob.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
