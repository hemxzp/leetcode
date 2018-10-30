# -*- coding:utf-8 _*_
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)-1):
            if i == 0 or nums[i] > nums[i - 1]:
                for j in self.threeSum(nums[i+1:],target-nums[i]):
                    tem=j.copy()
                    tem.append(nums[i])
                    if tem not in ans:
                        ans.append(tem)
        return ans
    def threeSum(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        dic=[]
        #nums.sort()
        for i in range (len(nums)-2):
            if i == 0 or nums[i] > nums[i - 1]:
                left=i+1
                right=len(nums)-1
                while left<right:
                    s= nums[i]+nums[left]+nums[right]
                    if s==target:

                        dic.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left <right and nums[left-1]==nums[left]:
                            left+=1
                        if right<len(nums)-1:
                            while left < right and nums[right+1]==nums[right]:
                                right-=1
                    if s>target:
                        right-=1
                    if s<target:
                        left+=1
        return dic
o=Solution()
print(o.fourSum([1, 0, -1, 0, -2, 2],0))