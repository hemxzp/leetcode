# -*- coding:utf-8 _*_
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic=[]
        nums.sort()
        for i in range (len(nums)-2):
            if i == 0 or nums[i] > nums[i - 1]:
                left=i+1
                right=len(nums)-1
                while left<right:
                    s= nums[i]+nums[left]+nums[right]
                    if s==0:

                        dic.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left <right and nums[left-1]==nums[left]:
                            left+=1
                        if right<len(nums)-1:
                            while left < right and nums[right+1]==nums[right]:
                                right-=1
                    if s>0:
                        right-=1
                    if s<0:
                        left+=1
        return dic
o=Solution()
print(o.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
