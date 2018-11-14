# -*- coding:utf-8 _*_
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=2:
            return 0
        m=[]
        h=0
        for i in range(len(height)):
            if height[i] >h:
                m=[]
                h=height[i]
            if height[i]==h:
                m.append(i)
        if len(m)>1:
            lefthigh=m[0]
            righthigh=m[-1]
        else:
            lefthigh=m[0]
            righthigh=m[0]
        ans=0
        if len(m)>1:
            for i in range(1,len(m)):
                ans+=self.trap2(m[i-1],m[i],h,height)
        left=0
        for i in range(1,lefthigh+1):
            if height[i]>height[left]:
                ans+=self.trap2(left,i,min(height[i],height[left]),height)
                left=i
        right=len(height)-1
        for i in range (len(height)-2,righthigh-1,-1):
            if height[i]>height[right]:
                ans+=self.trap2(i,right,min(height[i],height[right]),height)
                right=i
        return ans
    def trap2(self,a,b,h,height):
        count=0
        for i in range(a+1,b):
            count+=h-height[i]
        return count
o=Solution()
print(o.trap([0,1,0,2,1,0,1,3,2,1,2,1]))