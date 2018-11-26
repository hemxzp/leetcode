# -*- coding:utf-8 _*_
class Solution:

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        dic={}
        dic[0]=0
        dic[1]=0
        dic[2]=0
        for i in range(len(nums)):
            if nums[i]==0:
                tem=nums[dic[0]]
                nums[dic[0]]=0
                if tem==2:
                    nums[dic[2]]=2
                if tem==1:
                    tem2=nums[dic[1]]
                    nums[dic[1]]=1
                    if tem2==2:
                        nums[dic[2]]=2
                dic[0] += 1
                dic[1] += 1
                dic[2] += 1
                continue
            if nums[i]==1:
                tem=nums[dic[1]]
                nums[dic[1]]=1
                if tem==2:
                    nums[dic[2]]=2
                dic[1]+=1
                dic[2]+=1
                continue

            if nums[i]==2:
                dic[2]+=1
        return nums
o=Solution()
print(o.sortColors([2,0,2,1,1,0]))
