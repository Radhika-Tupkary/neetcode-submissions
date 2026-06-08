# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS using queue
        q = deque()
        if root:
            q.append(root)
        result = []

        while q:
            n = len(q)
            temp = []

            for _ in range(n):
                el = q.popleft()
                temp.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)

            result.append(temp)
            
            

        return result
        