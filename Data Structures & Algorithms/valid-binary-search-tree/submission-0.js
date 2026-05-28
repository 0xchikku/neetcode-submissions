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
     * @return {boolean}
     */
    isValidBST(root) {
        return this.validateWithBound(root)
    }

    // time - O(n), space - O(h)
    validateWithBound(root) {
        const isBST = (node, min, max) => {
            if (!node) return true;
            if (node.val <= min || node.val >= max) return false
            return isBST(node.left, min, node.val) && isBST(node.right, node.val, max)
        }
        return isBST(root, -Infinity, Infinity)
    }
}
