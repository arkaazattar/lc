# Last updated: 8/16/2026, 2:16:38 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        if len(intervals) == 1:
4            return intervals
5        
6        intervals.sort()
7        rsp = [intervals[0]]
8        
9        for i in range(1, len(intervals)):
10            # check if complete overlap
11            if rsp[-1][0] <= intervals[i][0] and rsp[-1][1] >= intervals[i][1]:
12                continue
13            if rsp[-1][1] >= intervals[i][0] and rsp[-1][1] <= intervals[i][1]:
14                rsp[-1][1] = intervals[i][1]
15            else:
16                rsp.append(intervals[i])
17        
18        return rsp
19
20