# -*- coding:utf-8 _*_
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        t=0
        ans=[]
        tem=[]
        lenth=maxWidth
        while t <len(words):
            if tem==[]:
                tem.append(words[t])
                lenth -= len(words[t])
                t+=1
            else:
                if lenth<len(words[t])+1:
                    ans.append(self.make(tem,maxWidth,lenth))
                    tem=[]
                    lenth=maxWidth
                else:
                    tem.append(words[t])
                    lenth-=len(words[t])+1
                    t+=1
        tem1 = tem[0]
        for i in range(1, len(tem)):
            tem1 = tem1 + ' ' + tem[i]
        tem1+=' '*lenth
        ans.append(tem1)
        return ans
    def make(self,tem,maxWidth,lenth):
        if len(tem)==1:
            return tem[0]+lenth*' '
        t=lenth//(len(tem)-1)
        d=lenth%(len(tem)-1)
        ans=tem[0]
        for i in range(d):
            ans=ans+' '*(1+t+1)+tem[1+i]
        for i in range(len(tem)-1-d):
            ans=ans+' '*(t+1)+tem[1+d+i]




        return ans
o=Solution()
print(o.fullJustify(["This"
"is"
"an"
"example"
"of"
"text"
"justification."],
16))