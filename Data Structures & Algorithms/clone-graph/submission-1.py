from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {node: Node(node.val)}  # dictionary with 1st original node and its clone
        q = deque([node])

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val) # create neighbor's clone first, before appending it as new clone's neighbor
                    q.append(nei)
                    
                old_to_new[cur].neighbors.append(old_to_new[nei])  # append neighbor's clone to new nodes neighbor's list

        return old_to_new[node]