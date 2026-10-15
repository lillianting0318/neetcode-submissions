# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_count = 0
        q = deque([(root, root.val)])

        while q:
            node, max_val = q.popleft()
            
            if node.val >= max_val:
                good_count += 1
            
            new_max = max(node.val, max_val)

            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))

        return good_count






