# -*- coding:utf-8 _*_
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans=''
        dic={}
        li=[]
        lenth=len(s)
        for i in t:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        t=False
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]-=1
                li.append(i)
                t=True
                for j in dic.values():
                    if j>0:
                        t=False
                        break
                if t:
                    break
        if not t:
            return ''
        else:
            v=0
            for i in range(len(li)):
                if dic[s[li[i]]]==0:
                    v=i
                    left=s[li[i]]
                    break
                else:
                    dic[s[li[i]]]+=1
            li=li[v:]
            lenth=li[-1]-li[0]+1
            ans=s[li[0]:li[-1]+1]


            for i in range(li[-1]+1,len(s)):
                if s[i] in dic:
                    li.append(i)
                    dic[s[i]]-=1
                    m=0
                    if s[i]==left:
                        for j in range(len(li)):
                            if dic[s[li[j]]]<0 :
                                m=j+1
                                dic[s[li[j]]]+=1
                            else:
                                break

                        li=li[m:]
                        left=s[li[0]]
                        tem=s[li[0]:li[-1]+1]
                        if len(tem)<lenth:
                            lenth=len(tem)
                            ans=tem
            return ans

o=Solution()
print(o.minWindow("cbbbacccccbbbacbabbabacbabbbabaacbaccccbcbcbcca",
"abcbcabaacccababacbabcacbc"))

