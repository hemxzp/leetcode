# -*- coding:utf-8 _*_
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        ans=[1]
        s='9'+s
        for i in range(1,len(s)):
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    ans.append(ans[-2])
                else:
                    return 0
            else:

                if s[i-1]=='1':
                    ans.append(ans[-1]+ans[-2])
                elif s[i-1]=='2':
                    if int(s[i])<7:
                        ans.append(ans[-1]+ans[-2])
                    else:
                        ans.append(ans[-1])
                else:
                    ans.append(ans[-1])
        return ans[-1]
o=Solution()
print(o.numDecodings('12120'))