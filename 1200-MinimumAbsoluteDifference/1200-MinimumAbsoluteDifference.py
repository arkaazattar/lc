# Last updated: 11/7/2026, 12:44:11 AM
1class Solution:
2    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
3        arr.sort()
4        min_diff = float("inf")
5
6        for i in range(1, len(arr)):
7            diff = arr[i] - arr[i - 1]
8            if diff < min_diff:
9                rsp = [[arr[i - 1], arr[i]]]
10                min_diff = diff
11                
12            elif diff == min_diff:
13                rsp.append([arr[i - 1], arr[i]])
14
15        return rsp