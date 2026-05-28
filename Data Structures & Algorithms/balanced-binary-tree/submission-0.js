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
    isBalanced(root) {
        const unbalanced = -1
        const calculateHeight = (node) => {
            if (!node) return 0
            const leftHeight = calculateHeight(node.left)
            const rightHeight = calculateHeight(node.right)

            if (leftHeight === unbalanced
            || rightHeight === unbalanced
            || Math.abs(leftHeight - rightHeight) > 1) {
                return unbalanced
            }

            return 1 + Math.max(leftHeight, rightHeight)
        }

        return calculateHeight(root) !== unbalanced
    }
}
