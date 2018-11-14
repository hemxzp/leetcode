# -*- coding:utf-8 _*_
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans=[]
        dic=[]
        for i in strs:
            if sorted(i) not in dic:
                dic.append(sorted(i))
                ans.append([i])
            else:
                ans[dic.index(sorted(i))].append(i)
        return ans
o=Solution()
print(o.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))