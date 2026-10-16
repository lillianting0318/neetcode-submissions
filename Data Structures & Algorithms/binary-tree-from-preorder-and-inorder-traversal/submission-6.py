# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use hashmap to find root in O(N)
        in_map = {}
        for i, v in enumerate(inorder):
            in_map[v] = i

        def helper(pre_start, pre_end, in_start, in_end):
            # Base case:
            if in_start > in_end or in_start > in_end:
                return None

            # First node of preorder is root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Look up the root in inorder and count left nodes
            mid = in_map[root_val]
            left_size = mid - in_start

            root.left = helper(
                pre_start + 1, 
                pre_start + left_size, 
                in_start,
                mid - 1)

            root.right = helper(
                pre_start + left_size + 1,
                pre_end,
                mid + 1,
                in_end
            )
            return root

        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)