# Last updated: 8/5/2026, 5:05:13 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        visited = set()
7        num_rows, num_cols = len(grid), len(grid[0])
8        islands = 0
9        
10        def bfs(r, c):
11            q = collections.deque()
12            visited.add((r, c))
13            q.append((r, c))
14
15            while q:
16                row, col = q.popleft()
17                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
18                for dr, dc in directions:
19                    r, c = row + dr, col + dc
20                    if (r in range(num_rows) and 
21                    c in range(num_cols) and 
22                    grid[r][c] == "1" and
23                    (r, c) not in visited):
24                        q.append((r, c))
25                        visited.add((r, c))
26
27        for r in range(num_rows):
28            for c in range(num_cols):
29                if grid[r][c] == "1" and (r, c) not in visited:
30                    bfs(r, c)
31                    islands += 1
32
33        return islands
34