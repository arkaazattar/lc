class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rsp = 0
        drs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(row, col):
            q = deque([(row, col)])
            while q:
                row, col = q.popleft()
                for dr, dc in drs:
                    r, c = row + dr, col + dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1":
                        q.append((r, c))
                        grid[r][c] = "0"
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    rsp += 1
        
        return rsp
