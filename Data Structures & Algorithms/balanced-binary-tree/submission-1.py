# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time - O(n), space - O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        self.unbalanced = -1
        def calcHeight(node):
            if not node: return 0
            left = calcHeight(node.left)
            right = calcHeight(node.right)
            if (left == self.unbalanced or right == self.unbalanced or abs(right - left) > 1): return self.unbalanced
            return 1 + max(left, right)

        return calcHeight(root) != self.unbalanced