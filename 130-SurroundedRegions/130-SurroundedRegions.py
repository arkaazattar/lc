# Last updated: 8/8/2026, 2:56:40 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        m, n = len(board), len(board[0])
        num_rows, num_cols = len(board), len(board[0])
        safe = set()

        def bfs(r, c):
            safe.add((r, c))
            q = collections.deque()
            q.append((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while q:
                row, col = q.popleft()
                
                for dr, dq in directions:
                    r, c = row + dr, col + dq
                    if r in range(num_rows) and c in range(num_cols) and (r, c) not in safe and board[r][c] == "O":
                        q.append((r, c))
                        safe.add((r, c)) 
        
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == 'O':
                    bfs(r, c)
        
        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"

        return board