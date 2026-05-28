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
     * @return {number[][]}
     */
    // time - O(n), space - O(w)
    levelOrder(root) {
        if (!root) return [];
        const res = [];
        const queue = [root];
        let cur = 0;
        while (cur < queue.length) {
            const levelNodes = [];
            const levelSize = queue.length;
            while (cur < levelSize) {
                const node = queue[cur++];
                levelNodes.push(node.val);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            res.push(levelNodes);
        }
        return res;
    }
}
