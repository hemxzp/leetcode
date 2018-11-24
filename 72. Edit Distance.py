# -*- coding:utf-8 _*_
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1=='':
            return len(word2)
        if word2=='':
            return len(word1)
        len1=len(word1)
        len2=len(word2)
        table=[]

        for i in range(len1):
            table.append([max(len1,len2)]*len2)
        add=0
        for i in range(len2):
            if word1[-1]!=word2[len2-1-i]:
                add+=1
                table[0][i]=add
            else:
                table[0][i]=add
                break
        t=i
        for i in range(t+1,len2):
            add+=1
            table[0][i]=add
        for i in range(1,len1):
            for j in range(len2):
                tem1=word1[-(1+i):]
                tem2=word2[-(1+j):]
                table[i][j]=self.check(tem1,tem2,table)
        return table[-1][-1]



    def check(self,word1,word2,table):
        len1=len(word1)
        len2=len(word2)
        if len2==1:
            if word2 in word1:
                return len1-1
            else:
                return len1

        t=0
        for i in range(min(len1, len2)):
            if word1[i] == word2[i]:
                t += 1
            else:
                break
        word1 = word1[t:]
        word2 = word2[t:]
        if word2=='':
            return len(word1)
        if word1=='':
            return len(word2)
        if t>0:
            return table[len1-1-t][len2-1-t]
        else:

            return 1+min(
                table[len1-2][len2-1],
                table[len1-1][len2-2],
                table[len1-2][len2-2]
                     )
o=Solution()
print(o.minDistance("invention",
""))