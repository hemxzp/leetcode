# -*- coding:utf-8 _*_
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words==[]:
            return []
        lenword=len(words[0])
        lenstr=len(s)
        lensubstr=len(words)*lenword
        times={}
        for i in words:
            if i in times:
                times[i]+=1
            else:
                times[i]=1

        ans=[]
        for i in range (lenstr-lensubstr+1):
            j=0
            cur={}
            while  j<len(words):
                word= s[i+j*lenword:i+j*lenword+lenword]
                if word in words:
                    if word in cur:
                        cur[word]+=1
                    else:
                        cur[word]=1
                    if cur[word]>times[word]:
                        break
                else:
                    break
                j+=1
            if j==len(words):
                ans.append(i)

        return ans
o= Solution()
print(o.findSubstring("barfoothefoobarman",["foo","bar"]))