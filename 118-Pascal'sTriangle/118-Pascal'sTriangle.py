# Last updated: 6/3/2026, 3:56:54 PM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        rsp = [[1]]
4        for _ in range(numRows - 1):
5            temp_row = [0] + rsp[-1] + [0]
6            row = []
7
8            for i in range(len(rsp[-1]) + 1):
9                row.append(temp_row[i] + temp_row[i + 1])
10            
11            rsp.append(row)
12        
13        return rsp
14
15