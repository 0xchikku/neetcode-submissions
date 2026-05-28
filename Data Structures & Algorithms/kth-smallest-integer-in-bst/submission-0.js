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
     * @param {number} k
     * @return {number}
     */
    // time - O(n), space - O(h)
    kthSmallest(root, k) {
        let visit = 0;
        const findK = (node) => {
            if (!node) return null;
            const left = findK(node.left);
            if (left !== null) return left;
            visit++;
            if (visit === k) return node.val;
            const right = findK(node.right)
            if (right !== null) return right
            return null;
        }
        return findK(root)
    }
}
