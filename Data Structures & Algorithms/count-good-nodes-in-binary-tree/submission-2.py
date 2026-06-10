# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return self.dfs(root, root.val)

    # time - O(n), space - O(h)
    def dfs(self, node, num):
        if not node: return 0
        max_num = max(node.val, num)
        left = self.dfs(node.left, max_num)
        right = self.dfs(node.right, max_num)
        return left + right + int(node.val >= num)