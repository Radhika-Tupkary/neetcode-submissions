# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(r, s):
            if r and s:
                if r.val == s.val:
                    return isSame(r.left, s.left) and isSame(r.right, s.right)
                else:
                    return False
            elif r or s:
                return False
            else:
                return True

        if not subRoot:
            return True
        if not root:
            return False

        if isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        