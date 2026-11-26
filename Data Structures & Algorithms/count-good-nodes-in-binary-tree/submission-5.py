# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                good = 1
            else:
                good = 0
            new_max = max(node.val, max_val)
            
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            return good

        return dfs(root, root.val)