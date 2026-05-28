/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        return this.dfs(root)
    }

    dfs(root) {
        if (!root) return null;
        [root.left, root.right] = [root.right, root.left];
        this.dfs(root.left)
        this.dfs(root.right)
        return root
    }

    bfs(root) {

    }
}
