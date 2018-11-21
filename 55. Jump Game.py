# -*- coding:utf-8 _*_
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]:
            return False
        if len(nums)==1:
            return True
        l=0
        while nums[l]>0:
            if l+nums[l]>=len(nums)-1:
                return True
            m=nums[l]
            t=l
            for i in range(1,nums[l]+1):
                if nums[i+l]+i>=m:
                    t=i+l
                    m=nums[i+l]+i
            l=t
            if l >=len(nums)-1:
                return True
        return False
o=Solution()
print(o.canJump([0]))