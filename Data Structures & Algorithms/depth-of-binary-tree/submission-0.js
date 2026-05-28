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
     * @return {number}
     */
    maxDepth(root) {
        return this.dfs(root)
    }

    dfs(root) {
        if (!root) return 0
        return Math.max(this.dfs(root.left), this.dfs(root.right)) + 1
    }

    bfs(root) {

    }
}
