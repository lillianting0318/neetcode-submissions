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

            # Check if the current node is "good"
            is_good = 1 if node.val >= max_val else 0

            # Update the max value
            new_max = max(node.val, max_val)

            # Recurse down left and right subtrees and sum the counts
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)
