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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        if (!root) return null
        const small = Math.min(p.val, q.val);
        const large = Math.max(p.val, q.val);
        // return this.dfs(root, small, large);
        return this.iterative(root, small, large);

    }

    // time - O(h), space - O(h)
    dfs(root, small, large) {
        console.log({small, large, root})
        if (small <= root.val && root.val <= large) return root;
        if (small > root.val) return this.dfs(root.right, small, large);
        if (large < root.val) return this.dfs(root.left, small, large);
    }

    // time - O(h), space - O(1)
    iterative(root, small, large) {
        while (root) {
            if (small > root.val) root = root.right;
            else if (large < root.val) root = root.left;
            else return root;
        }
        return null;
    }
}
