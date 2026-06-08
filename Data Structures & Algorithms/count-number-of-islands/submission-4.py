from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def explore_dfs_recursion(i, j):
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

        def explore_bfs_queue(l, m):
            q = deque()
            q.append((l,m))
            while q:
                (l, m) = q.popleft()
                visited.add((l, m))
                if l+1 < rows and grid[l+1][m] == "1" and (l+1, m) not in visited:
                    q.append((l+1, m))
                if l-1 >= 0 and grid[l-1][m] == "1" and (l-1, m) not in visited:
                    q.append((l-1, m))
                if m+1 < cols and grid[l][m+1] == "1" and (l, m+1) not in visited:
                    q.append((l, m+1))
                if m-1 >= 0 and grid[l][m-1] == "1" and (l, m-1) not in visited:
                    q.append((l, m-1))

                
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    # explore_dfs_recursion(row, col)
                    explore_bfs_queue(row, col)

        return islands

        
