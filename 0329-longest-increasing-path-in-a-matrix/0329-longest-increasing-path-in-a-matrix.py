class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in dp:
                return dp[(r, c)]

            max_len = 1
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            dp[(r, c)] = max_len
            return max_len

        longest_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                longest_path = max(longest_path, dfs(r, c))

        return longest_path