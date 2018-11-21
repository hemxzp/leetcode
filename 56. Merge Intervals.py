# -*- coding:utf-8 _*_
#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals==[]:
            return []
        intervals.sort(key=lambda a:a.start)
        ans=[]
        tem=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i].start<=tem.end:
                if intervals[i].end>tem.end:
                    tem.end=intervals[i].end
            else:
                ans.append(tem)
                tem=intervals[i]
        ans.append(tem)
        return ans


a=[]
test=[]
for i in a:
    tem=Interval()
    tem.start=i[0]
    tem.end=i[1]
    test.append(tem)
o=Solution()
a=o.merge(test)
for i in a:
    print(i.start,i.end)
