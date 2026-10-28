# Last updated: 10/27/2026, 9:13:50 PM
1class Solution:
2    def isValidSudoku(self, board: list[list[str]]) -> bool:
3        # three checks per number
4        # 1. Has the number been seen in this row? 
5        # 2. Has the number been seen in this column?
6        # 3. Has the number been seen in this sub-box?
7        seen_rows = [set() for _ in range(9)]
8        seen_cols = [set() for _ in range(9)]
9        seen_sub_boxes = [set() for _ in range(9)]
10        
11        for row in range(9):
12            for col in range(9):
13                num = board[row][col]
14                if num == '.':
15                    continue
16                box = (row // 3) * 3 + (col // 3)
17                if num in seen_rows[row]:
18                    return False
19                elif num in seen_cols[col]:
20                    return False
21                elif num in seen_sub_boxes[box]:
22                    return False
23                seen_sub_boxes[box].add(num)
24                seen_rows[row].add(num)
25                seen_cols[col].add(num)
26            
27        return True
28                