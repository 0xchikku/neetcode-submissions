# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time - O(n), space - O(h)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -math.inf
        def recursion(node: Optional[TreeNode]) -> int:
            if not node: return 0
            left = max(0, recursion(node.left))
            right = max(0, recursion(node.right))
            self.maxPath = max(self.maxPath, left + right + node.val)
            return node.val + max(left, right)

        recursion(root)
        return self.maxPath