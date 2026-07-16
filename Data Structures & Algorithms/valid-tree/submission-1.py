from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. No cycles
        # 2. len(edges) == n-1
        # 3. len(visited) == n  (connected)

        if len(edges) != n-1:
            return False

        q = deque()
        graph = {i:[] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        q = deque([(0, -1)])

        while q:
            node, parent = q.popleft()

            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                q.append((nei, node))

        return len(visited) == n
        
        