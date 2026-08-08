# Last updated: 8/8/2026, 2:56:33 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        num_rows, num_cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(num_rows) and 
                    c in range(num_cols) and 
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
