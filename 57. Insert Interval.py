# -*- coding:utf-8 _*_
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans=[]
        for i in range(len(intervals)):
            if intervals[0].end>=newInterval.start:
                break
            else:
                ans+=[intervals.pop(0)]
        if intervals==[]:
            return ans+[newInterval]
        tem=Interval()
        tem.start=min(intervals[0].start,newInterval.start)
        tem.end=newInterval.end
        while intervals[0].start<=newInterval.end:
            if intervals[0].end>newInterval.end:
                if intervals[0].start<=tem.end:
                    tem.end=intervals.pop(0).end
                break
            else:
                intervals.pop(0)
            if intervals==[]:
                break
        ans +=[tem]
        return ans + intervals
a=[[1,2],[3,5],[6,7],[8,10],[12,16]]
test=[]
aa=Interval()
aa.start=18
aa.end=20
for i in a:
    tem=Interval()
    tem.start=i[0]
    tem.end=i[1]
    test.append(tem)
o=Solution()
a=o.insert(test,aa)
for i in a:
    print(i.start,i.end)

