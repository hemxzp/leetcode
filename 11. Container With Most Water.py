# -*- coding:utf-8 _*_
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m=0
        l=0
        r=len(height)-1
        while l!=r:
            m=max(m,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return (m)
o=Solution()
print(o.maxArea([1,8,6,2,5,4,8,3,7]))





    #暴力搜索

'''
        m=0
        for i in range(len(height)-1):
            l=0
            for j in range(len(height)-1,i,-1):
                if height[j]>l:
                    s=min(height[i],height[j])*(j-i)
                    if s>m:
                        m=s
                        l=height[j]
        return m
        '''