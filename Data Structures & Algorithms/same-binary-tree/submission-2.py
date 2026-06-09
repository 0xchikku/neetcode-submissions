# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
        # return self.bfs(p, q)

    # time - O(n), space - O(h)
    def dfs(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)

    # time - O(n), space - O(w)
    def bfs(self, p, q):
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if (not node1 and not node2): continue
            if (not node1 or not node2 or node1.val != node2.val): return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        return True