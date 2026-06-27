# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check_kids(r1, r2):
            if r1 and r2:
                if r1.val != r2.val:
                    return False
            elif r1 and not r2:
                return False
            elif r2 and not r1:
                return False
            else:
                return True
            
            return check_kids(r1.left, r2.left) and check_kids(r1.right, r2.right)

        return check_kids(p, q)
        