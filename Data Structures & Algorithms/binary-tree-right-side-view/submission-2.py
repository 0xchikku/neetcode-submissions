# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        # return self.bfs(root)
        return self.dfs(root)
    
    # time - O(n), space - O(h)
    def dfs(self, root):
        res = []
        def recursion(node, depth):
            if not node: return
            if depth == len(res): res.append(node.val)
            recursion(node.right, depth + 1)
            recursion(node.left, depth + 1)
        recursion(root, 0)
        return res

    # time - O(n), space - O(h)
    def bfs(self, root):
        res = []
        queue = deque([root])
        while queue:
            level = len(queue)
            end = queue[-1]
            res.append(end.val)
            for i in range(level):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
