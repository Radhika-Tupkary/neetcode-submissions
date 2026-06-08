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
        # result = []
        # q = deque()
        # q.append(root)
        
        # while q:
        #     n = len(q)
        #     temp = []

        #     for _ in range(n):
        #         el = q.popleft()
        #         if el:
        #             temp.append(el.val)
        #             q.append(el.left)
        #             q.append(el.right)

        #     if temp:
        #         result.append(temp)

        # return result

        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
        