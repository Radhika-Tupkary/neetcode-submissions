from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def explore_bfs_queue(l, m):
            q = deque()
            curr_area = 1
            q.append((l,m))
            visited.add((l, m))

            while q:
                (l, m) = q.popleft()
                
                if l+1 < rows and grid[l+1][m] == 1 and (l+1, m) not in visited:
                    q.append((l+1, m))
                    visited.add((l+1, m))
                    curr_area += 1
                if l-1 >= 0 and grid[l-1][m] == 1 and (l-1, m) not in visited:
                    q.append((l-1, m))
                    visited.add((l-1, m))
                    curr_area += 1
                if m+1 < cols and grid[l][m+1] == 1 and (l, m+1) not in visited:
                    q.append((l, m+1))
                    visited.add((l, m+1))
                    curr_area += 1
                if m-1 >= 0 and grid[l][m-1] == 1 and (l, m-1) not in visited:
                    q.append((l, m-1))
                    visited.add((l, m-1))
                    curr_area += 1

            return curr_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = explore_bfs_queue(i, j)
                    print("area", area)
                    print("maxArea", maxArea)
                    maxArea = max(maxArea, area)


        return maxArea


