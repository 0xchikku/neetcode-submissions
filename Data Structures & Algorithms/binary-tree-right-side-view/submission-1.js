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
        if (!root) return [];
        // return this.bfs(root);
        return this.dfs(root);
    }

    // time - O(n), space - O(h)
    dfs(root) {
        const res = [];
        const visitNode = (node, depth) => {
            if (!node) return;
            if (depth === res.length) res.push(node.val);
            visitNode(node.right, depth+1);
            visitNode(node.left, depth+1);
        }
        visitNode(root, 0);
        return res;
    }

    // time - O(n), space - O(w)
    bfs(root) {
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
