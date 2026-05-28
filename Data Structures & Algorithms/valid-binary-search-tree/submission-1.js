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
        // return this.validateWithBound(root)
        return this.inorder(root)
    }

    // time - O(n), space - O(n)
    inorder(root) {
        let prev = -Infinity;
        const isBST = (node) => {
            if (!node) return true;
            if (!isBST(node.left)) return false;
            if (node.val <= prev) return false;
            prev = node.val;
            if (!isBST(node.right)) return false;
            return true;
        }
        return isBST(root)
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
