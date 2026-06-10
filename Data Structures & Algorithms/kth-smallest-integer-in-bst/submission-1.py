# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time - O(n), space - O(h)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.visit = 0
        def recursion(node):
            if not node: return None
            left = recursion(node.left)
            if left != None: return left
            self.visit += 1
            if self.visit == k: return node.val
            right = recursion(node.right)
            if right != None: return right
            return None
        return recursion(root)
