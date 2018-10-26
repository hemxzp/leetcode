# -*- coding:utf-8 _*_
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        if '' in strs:
            return ''

        t=-1
        end=False
        while True:
            if t + 1 == len(strs[0]):
                end = True
                break
            k=strs[0][t+1]
            for i in strs:
                if  t+1==len(i)  :
                    end=True
                    break
                else:
                    if  i[t+1]!=k:
                        end=True
                        break
            if not end:
                t+=1
            else:
                break

        if t==-1:
            return ''
        else:
            return strs[0][:t+1]
            #return t

o=Solution()
print(o.longestCommonPrefix(['a']))