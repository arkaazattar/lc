class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rsp = 0
        seen = set()

        def bfs(row, col):
            seen.add((row, col))
            q = collections.deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = row + dr, col + dc
                    if (
                        r < 0
                        or c < 0
                        or r >= len(grid)
                        or c >= len(grid[0])
                        or (r, c) in seen
                        or grid[r][c] != "1"
                    ):
                        continue
                    seen.add((r, c))
                    q.append((r, c))
            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] == "1":
                    bfs(row, col)
                    rsp += 1

        return rsp
