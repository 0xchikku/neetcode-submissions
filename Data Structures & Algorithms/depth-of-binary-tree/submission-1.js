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
    maxDepth(root) {
        // return this.dfs(root)
        return this.bfs(root)
    }

    dfs(root) {
        if (!root) return 0
        return Math.max(this.dfs(root.left), this.dfs(root.right)) + 1
    }

    bfs(root) {
        let depth = 0
        if (!root) return depth

        const queue = [root]
        let cur = 0

        while(cur < queue.length) {
            const levelWidth = queue.length
            while (cur < levelWidth) {
                const node = queue[cur++]
                if (node.left) queue.push(node.left)
                if (node.right) queue.push(node.right)
            }
            depth++
        }

        return depth
    }
}
