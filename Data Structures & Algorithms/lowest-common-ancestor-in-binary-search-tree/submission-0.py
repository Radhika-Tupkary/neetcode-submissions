# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        road1 = [root]
        curr = root
        while curr.val != p.val:
            if p.val > curr.val:
                curr = curr.right
                road1.append(curr)
            else:
                curr = curr.left
                road1.append(curr)
        road2 = [root]
        curr = root
        while curr.val != q.val:
            if q.val > curr.val:
                curr = curr.right
                road2.append(curr)
            else:
                curr = curr.left
                road2.append(curr)

        for el1 in reversed(road1):
            for el2 in reversed(road2):
                if el1 == el2:
                    return el1
        


        