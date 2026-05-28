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
    goodNodes(root) {
        if (!root) return null
        const countGoodNodes = (node, maxSeen) => {
            if (!node) return 0;
            const isGood = node.val >= maxSeen;
            maxSeen = Math.max(maxSeen, node.val);
            const left = countGoodNodes(node.left, maxSeen);
            const right = countGoodNodes(node.right, maxSeen);
            return Number(isGood) + left + right;
        }
        return countGoodNodes(root, root.val)
    }
}
