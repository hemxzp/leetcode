# -*- coding:utf-8 _*_
class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t=[]
        for i in s :
            if i =='{':
                t.append('{')
            if i == '(':
                t.append('(')
            if i== '[':
                t.append('[')
            if i == '}':
                if bool(t):
                    if t[len(t)-1]=='{':
                        t.pop()
                    else:
                        return False

                else:
                    return False
            if i == ']':
                if bool(t):
                    if t[len(t) - 1] == '[':
                        t.pop()
                    else:
                        return False

                else:
                    return False
            if i == ')':
                if bool(t):
                    if t[len(t) - 1] == '(':
                        t.pop()
                    else:
                        return False

                else:
                    return False
        return not bool(t)

o=Solution()
print(o.isValid('()'))



