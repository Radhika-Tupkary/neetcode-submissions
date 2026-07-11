class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node, maxSoFar):
            if not node:
                return 0
            
            res = 0
            if node.val >= maxSoFar:
                res = 1
            
            numLeft = count(node.left, max(node.val, maxSoFar))
            numRight = count(node.right, max(node.val, maxSoFar))
            return res + numLeft + numRight
            
                 
        return count(root, root.val)