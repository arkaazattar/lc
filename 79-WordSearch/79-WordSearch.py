# Last updated: 8/9/2026, 5:07:10 PM
class Solution:

    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            # Entire word matched
            if index == len(word):
                return True

            # Invalid position
            if (
                r < 0 or
                r >= rows or
                c < 0 or
                c >= cols
            ):
                return False

            # Character mismatch
            if board[r][c] != word[index]:
                return False

            # Save original character
            temp = board[r][c]

            # Mark visited
            board[r][c] = "#"

            # Explore 4 directions
            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

            # Undo (Backtracking)
            board[r][c] = temp

            return found

        # Try every cell as starting point
        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False

        #retry again