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
     * @return {TreeNode}
     */
    invertTree(root) {
        return this.bfs(root)
        // return this.dfs(root)
    }

    dfs(root) {
        if (!root) return null;
        [root.left, root.right] = [root.right, root.left];
        this.dfs(root.left)
        this.dfs(root.right)
        return root
    }

    bfs(root) {
        if (!root) return null
        const queue = [root]
        let cur = 0

        while(cur < queue.length) {
            const node = queue[cur++];
            [node.left, node.right] = [node.right, node.left];
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)            
        }

        return root
    }
}
