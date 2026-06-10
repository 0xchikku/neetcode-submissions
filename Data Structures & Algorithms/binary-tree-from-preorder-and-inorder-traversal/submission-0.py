# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time - O(n), space - O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {}
        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i
        
        def recursion(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end: return None
            root = TreeNode(preorder[pre_start])
            mid = inorder_index_map[preorder[pre_start]]
            left_subtree_len = mid - in_start
            root.left = recursion(pre_start+1, pre_start+left_subtree_len, in_start, mid-1)
            root.right = recursion(pre_start+left_subtree_len+1, pre_end, mid+1, in_end)
            return root
        
        return recursion(0, len(preorder)-1, 0, len(inorder)-1)