from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        # Python Common Bug #8: Marking Visited After Dequeue Instead of Before Enqueue
        # For BFS,
        # viited.add(neighbor)   # Mark first
        # q.append(neighbor)      # Then enqueue

        def explore_bfs_queue(l, m):

            q = deque()
            curr_area = 1
            visited.add((l, m))
            q.append((l,m))

            while q:
                (l, m) = q.popleft()
                
                if l+1 < rows and grid[l+1][m] == 1 and (l+1, m) not in visited:
                    visited.add((l+1, m))
                    q.append((l+1, m))
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

        def explore(i, j):
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                grid[i][j] == 0 or
                (i, j) in visited
            ):
                return 0

            visited.add((i, j))
            return (1 + explore(i + 1, j) + explore(i - 1, j) + explore(i, j + 1) + explore(i, j - 1))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, explore_bfs_queue(i, j))
                    # maxArea = max(maxArea, explore(i, j))


        return maxArea