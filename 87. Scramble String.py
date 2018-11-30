# -*- coding:utf-8 _*_
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        tem1={}
        tem2={}
        if s1=='' or s1==s2:
            return True
        for i in range (len(s1)-1):
            if s1[i] not in tem1:
                tem1[s1[i]]=1
            else:
                tem1[s1[i]]+=1
            if s1[-1-i] not in tem2:
                tem2[s1[-1-i]]=1
            else:
                tem2[s1[-1-i]]+=1

            if s2[i] in tem1:
                tem1[s2[i]]-=1
            else:
                tem1[s2[i]]=-1
            if s2[i] in tem2:
                tem2[s2[i]]-=1
            else:
                tem2[s2[i]]=-1
            t=True
            for j in tem1.values():
                if j!=0:
                    t=False
                    break
            if t:
                if self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:]):
                    return True
            t = True
            for j in tem2.values():
                if j != 0:
                    t = False
                    break
            if t:
                if self.isScramble(s1[-i-1:],s2[:i+1]) and self.isScramble(s1[:-i-1],s2[i+1:]):
                    return True
        return False
o=Solution()
print(o.isScramble('abcde','caedb'))