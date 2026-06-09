# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        # return self.dfs(root)
        return self.bfs(root)
    
    # time - O(n), space - O(w)
    def bfs(self, root):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root

    # time - O(n), space - O(h)
    def dfs(self, root):
        if not root: return
        root.left, root.right = root.right, root.left
        self.dfs(root.left)
        self.dfs(root.right)
        return root


