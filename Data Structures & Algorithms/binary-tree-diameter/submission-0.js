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
    diameterOfBinaryTree(root) {
        let maxDiameter = 0
        const calculateHeight = (node) => {
            if (!node) return 0
            const leftHeight = calculateHeight(node.left)
            const rightHeight = calculateHeight(node.right)
            maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight)
            return 1 + Math.max(leftHeight, rightHeight)
        }
        calculateHeight(root)
        return maxDiameter
    }
}
