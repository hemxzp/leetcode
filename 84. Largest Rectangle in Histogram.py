# -*- coding:utf-8 _*_
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        n = len(height)

        # left[i], right[i] represent how many bars are >= than the current bar

        left = [1] * n
        right = [1] * n
        max_rect = 0

        # calculate left
        for i in range(0, n):
            j = i - 1
            while j >= 0:
                if height[j] >= height[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break

        # calculate right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if height[j] >= height[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            max_rect = max(max_rect, height[i] * (left[i] + right[i] - 1))

        return max_rect
class Solution(object):
    def largestRectangleArea(self, heights):
        ans = 0
        st = []
        for x in heights + [0]:
            count = 0
            while st and st[-1][0] > x:
                y,ycount = st.pop()
                count += ycount
                ans = max(ans, y*count)
            st += [[x, count+1]]
        return ans

o=Solution()
print(o.largestRectangleArea([i for i in range (20000,-1,-1)]))