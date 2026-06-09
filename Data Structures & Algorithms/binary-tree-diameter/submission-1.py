# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time - O(n), space - O(h)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.maxDiameter = 0

        def calcHeight(node):
            if not node: return 0
            left = calcHeight(node.left)
            right = calcHeight(node.right)
            self.maxDiameter = max(self.maxDiameter, left+right)
            return 1 + max(left, right)
        
        calcHeight(root)
        return self.maxDiameter
        
