# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # time - O(n), space - O(n)
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs(node):
            if not node: 
                preorder.append('n')
                return
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(preorder)
        
    # Decodes your encoded data to tree.
    # time - O(n), space - O(n)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        self.index = 0
        def recursion():
            cur = preorder[self.index]
            self.index += 1
            if cur == 'n': 
                return None
            node = TreeNode(int(cur))
            node.left = recursion()
            node.right = recursion()
            return node
        return recursion()
