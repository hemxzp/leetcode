# -*- coding:utf-8 _*_
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return 1
        left=0
        ans=1
        end=len(nums)-1
        while  left+nums[left]<end:
            ans+=1
            m=0
            tem=left
            for i in range(left+1,left+nums[left]+1):
                if i+nums[i]>m:
                    m=i+nums[i]
                    tem=i
            left=tem

        return ans
o=Solution()
print(o.jump([2,3,1,1,4]))