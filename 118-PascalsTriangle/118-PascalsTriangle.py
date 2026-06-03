# Last updated: 6/3/2026, 4:01:38 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rsp = [[1]]
        for _ in range(numRows - 1):
            temp_row = [0] + rsp[-1] + [0]
            row = []

            for i in range(len(rsp[-1]) + 1):
                row.append(temp_row[i] + temp_row[i + 1])
            
            rsp.append(row)
        
        return rsp

