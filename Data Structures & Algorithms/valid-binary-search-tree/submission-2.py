# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.with_bound(root)
        return self.with_prev(root)

    # time - O(n), space - O(h)
    def with_prev(self, root):
        self.prev = -math.inf
        def recursion(node):
            if not node: return True
            if not recursion(node.left): return False
            if node.val <= self.prev: return False
            self.prev = node.val
            if not recursion(node.right): return False
            return True
        return recursion(root)

    # time - O(n), space - O(h)
    def with_bound(self, root):
        small = -math.inf
        large = math.inf
        def is_bst(node, small, large):
            if not node: return True
            if node.val <= small or node.val >= large: return False
            return is_bst(node.left, small, node.val) and is_bst(node.right, node.val, large)

        return is_bst(root, small, large)