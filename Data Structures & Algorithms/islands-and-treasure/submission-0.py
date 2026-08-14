from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        while q:
            m, n =  q.popleft()
            # (m+1, n), (m-1, n), (m, n+1), (m, n-1)
            if m+1 < rows and grid[m+1][n] == INF:
                grid[m+1][n] = grid[m][n] + 1
                q.append((m+1, n))
            
            if m-1 >= 0 and grid[m-1][n] == INF:
                grid[m-1][n] =  grid[m][n] + 1
                q.append((m-1, n))

            if n+1 < cols and grid[m][n+1] == INF:
                grid[m][n+1] =  grid[m][n] + 1
                q.append((m, n+1))

            if n-1 >= 0 and grid[m][n-1] == INF:
                grid[m][n-1] =  grid[m][n] + 1
                q.append((m, n-1))

            

        


        