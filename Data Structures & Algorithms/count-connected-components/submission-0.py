from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0
        nodeToEdges = defaultdict(list)

        for edge in edges:
            nodeToEdges[edge[0]].append(edge[1])
            nodeToEdges[edge[1]].append(edge[0])

        # {
        #     0: [1],
        #     1: [0,2],
        #     2: [1],
        #     3: [4],
        #     4: [3],
        # }

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in nodeToEdges[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
        