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
     * @return {number[]}
     */
    rightSideView(root) {
        return this.bfs(root);
    }

    bfs(root) {
        if (!root) return [];
        const res = [];
        let cur = 0;
        const queue = [root];
        while (cur < queue.length) {
            const levelEnd = queue.length;
            while (cur < levelEnd) {
                const node = queue[cur++];
                if (cur === levelEnd) res.push(node.val);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
        }
        return res;
    }
}
