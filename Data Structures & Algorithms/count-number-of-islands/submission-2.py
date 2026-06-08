class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def explore(i, j):
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                grid[i][j] == "0" or
                (i, j) in visited
            ):
                return

            visited.add((i, j))
            explore(i + 1, j)
            explore(i - 1, j)
            explore(i, j + 1)
            explore(i, j - 1)

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    explore(row, col)

        return islands

        
