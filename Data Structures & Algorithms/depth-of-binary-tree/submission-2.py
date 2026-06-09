# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.dfs(root)
        # return self.bfs(root)

    # time - O(n), space - O(h)
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return 1 + max(left, right)
    
    # time - O(n), space - O(w)
    def bfs(self, root):
        if not root: return 0
        depth = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if (node.left): queue.append(node.left)
                if (node.right): queue.append(node.right)
            depth += 1
        return depth
