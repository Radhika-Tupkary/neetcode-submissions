from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {node: Node(node.val)}  # dictionary with 1st original node and its clone
        q = deque([node])                    # q with 1st original node

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if nei not in old_to_new:
                    # create neighbor's clone first, before appending it as new clone's neighbor
                    old_to_new[nei] = Node(nei.val) 
                    q.append(nei)

                # append neighbor's clone to clone of cur node's neighbor's list
                old_to_new[cur].neighbors.append(old_to_new[nei])  

        return old_to_new[node]