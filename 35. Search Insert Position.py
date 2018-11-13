# -*- coding:utf-8 _*_
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return 0
        for i in range (len(nums)):
            if target<=nums[i]:
                return i
        return len(nums)
o=Solution()
print(o.searchInsert( [1,3,5,6], 0))