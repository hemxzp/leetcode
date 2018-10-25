# -*- coding:utf-8 _*_
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        add=0
        if s[0]=='M':
            for i in s:
                if i=='M':
                    add+=1
                else:
                    break
            s=s[add:]
        ans+=add*1000
        add=0
        if s=="":
            return ans
        if s[0]=='D':
            add=5
            for i in s[1:]:
                if i=='C':
                    add+=1
                else:
                    break
            s=s[add-4:]
        ans += add * 100
        add=0
        if s == "":
            return ans
        if s[0]=='C':
            add=0
            for i in s:
                if i=='C':
                    add+=1
                else:
                    break
            s=s[add:]
            if s[0:1]=='D':
                add=4
                s=s[1:]
            if s[0:1]=='M':
                add=9
                s=s[1:]
        ans+=add*100
        add=0
        if s=='':
            return ans
        if s[0]=='L':
            add=5
            for i in s[1:]:
                if i=='X':
                    add+=1
                else:
                    break
            s=s[add-4:]
        ans += add * 10
        add=0
        if s == "":
            return ans
        if s[0]=='X':
            add=0
            for i in s:
                if i=='X':
                    add+=1
                else:
                    break
            s=s[add:]
            if s[0:1]=='L':
                add=4
                s=s[1:]
            if s[0:1]=='C':
                add=9
                s=s[1:]
        ans+=add*10
        add=0
        if s=='':
            return ans
        if s[0]=='V':
            add=5
            for i in s[1:]:
                if i=='I':
                    add+=1
                else:
                    break
            s=s[add-4:]
        ans += add * 1
        add=0
        if s == "":
            return ans
        if s[0]=='I':
            add=0
            for i in s:
                if i=='I':
                    add+=1
                else:
                    break
            s=s[add:]
            if s[0:1]=='V':
                add=4
                s=s[1:]
            if s[0:1]=='X':
                add=9
                s=s[1:]
        ans+=add
        return (ans)
o=Solution()
print(o.romanToInt("LVIII"))

