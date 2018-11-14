# -*- coding:utf-8 _*_
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans=[]
        dic={}
        for i in strs:
            s=''.join(sorted(i))
            if s not in dic:
                dic[s]=[i]

            else:
                dic[s].append(i)
        for i in dic.values():
            ans.append(i)
        return ans
o=Solution()
print(o.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))