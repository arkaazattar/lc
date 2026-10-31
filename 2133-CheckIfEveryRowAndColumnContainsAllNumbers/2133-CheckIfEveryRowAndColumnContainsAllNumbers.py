# Last updated: 10/31/2026, 6:28:43 PM
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        seen_cols = [set() for _ in range(n)]
        for row in range(n):
            seen_rows = set() 
            for col in range(n):
                num = matrix[row][col]
                if num in seen_rows:
                    return False
                if num in seen_cols[col]:
                    return False
                seen_rows.add(num)
                seen_cols[col].add(num)

        return True
