# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # Step 1: Traverse to the leftmost node along the current path
            while curr:
                stack.append(curr)
                curr = curr.left

            # Step 2: Pop the smallest remaining element
            curr = stack.pop()
            k -= 1

            # Step 3: If k reaches 0, we found the kth smallest node
            if k == 0:
                return curr.val

            # Step 4: Explore the right subtree
            curr = curr.right
