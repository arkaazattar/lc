# Last updated: 10/27/2026, 8:05:49 PM
1class Solution:
2    def isValidSudoku(self, board: list[list[str]]) -> bool:
3        # three checks per number
4        # 1. Has the number been seen in this row? Done
5        # 2. Has the number been seen in this column?
6        # 3. Has the number been seen in this sub-box Done
7        num_rows, num_cols = 9, 9
8        sub_boxes = [set() for _ in range(9)]
9        cols = [set() for _ in range(9)]
10        def check_sub_box(row, col, num):
11            print(row, col)
12            if row in {0, 1, 2}:
13                if col in {0, 1, 2}:
14                    if num in sub_boxes[0]:
15                        return False
16                    sub_boxes[0].add(num)
17                elif col in {3, 4, 5}:
18                    if num in sub_boxes[1]:
19                        return False
20                    sub_boxes[1].add(num)
21                elif col in {6, 7, 8}:
22                    if num in sub_boxes[2]:
23                        return False
24                    sub_boxes[2].add(num)
25            if row in {3, 4, 5}:
26                if col in {0, 1, 2}:
27                    if num in sub_boxes[3]:
28                        return False
29                    sub_boxes[3].add(num)
30                elif col in {3, 4, 5}:
31                    if num in sub_boxes[4]:
32                        return False
33                    sub_boxes[4].add(num)
34                elif col in {6, 7, 8}:
35                    if num in sub_boxes[5]:
36                        return False
37                    sub_boxes[5].add(num)
38            if row in {6, 7, 8}:
39                if col in {0, 1, 2}:
40                    if num in sub_boxes[6]:
41                        return False
42                    sub_boxes[6].add(num)
43                elif col in {3, 4, 5}:
44                    if num in sub_boxes[7]:
45                        return False
46                    sub_boxes[7].add(num)
47                elif col in {6, 7, 8}:
48                    if num in sub_boxes[8]:
49                        return False
50                    sub_boxes[8].add(num)
51            return True
52
53        for row in range(num_rows):
54            cur_row = set()
55            for col in range(num_cols):
56                num = board[row][col]
57                if num == '.':
58                    continue
59                if not check_sub_box( row, col, num):
60                    return False
61                if num in cur_row:
62                    return False
63                cur_row.add(board[row][col])
64                if num in cols[col]:
65                    return False
66                cols[col].add(num)
67
68        print(sub_boxes)
69        return True
70        
71