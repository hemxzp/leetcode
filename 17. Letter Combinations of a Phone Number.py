# -*- coding:utf-8 _*_
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        dic={'2':"abc",'3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        o=[]
        ans=[]
        tem=''
        for i in digits:
            res.append(0)
            o.append(len(dic[i])-1)
            tem+=dic[i][0]
        ans.append(tem)
        while res!=o:
            t=0
            res[0]+=1
            while res[t]==len(dic[digits[t]]):
                res[t]=0
                res[t+1]+=1
                t+=1
            tem=''
            for i in range(len(res)):
                tem+=dic[digits[i]][res[i]]
            ans.append(tem)
        return ans
o=Solution()
print(o.letterCombinations('23'))