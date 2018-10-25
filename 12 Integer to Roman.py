# -*- coding:utf-8 _*_
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=str(num)
        ss=''
        if len(s)==4:
            ss+=int(s[0])*'M'
            s=s[1:]
        if len(s)==3:
            if int(s[0])<4:
                ss+=int(s[0])*'C'
            if int(s[0])==4:
                ss+='CD'
            if int(s[0])>=5 and int(s[0])<9:
                ss=ss+'D'+'C'*(int(s[0])-5)
            if int(s[0])==9:
                ss+='CM'
            s=s[1:]
        if len(s)==2:
            if int(s[0])<4:
                ss+=int(s[0])*'X'
            if int(s[0])==4:
                ss+='XL'
            if int(s[0])>=5 and int(s[0])<9:
                ss=ss+'L'+'X'*(int(s[0])-5)
            if int(s[0])==9:
                ss+='XC'
            s=s[1:]
        if len(s)==1:
            if int(s[0])<4:
                ss+=int(s[0])*'I'
            if int(s[0])==4:
                ss+='IV'
            if int(s[0])>=5 and int(s[0])<9:
                ss=ss+'V'+'I'*(int(s[0])-5)
            if int(s[0])==9:
                ss+='IX'

        return (ss)
o=Solution()
print(o.intToRoman(1994))
