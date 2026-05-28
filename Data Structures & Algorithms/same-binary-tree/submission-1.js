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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        // return this.dfs(p, q)
        return this.bfs(p, q)
    }

    dfs(p, q) {
        if (!p && !q) return true
        if (!p || !q || p.val !== q.val) return false
        return this.dfs(p.left, q.left) && this.dfs(p.right, q.right)
    }

    bfs(p, q) {
        let curNode = 0
        const queue = [[p,q]]
        while (curNode < queue.length) {
            const [node1, node2] = queue[curNode++]
            if (!node1 && !node2) continue
            if (!node1 || !node2 || node1.val !== node2.val) return false
            queue.push([node1.left, node2.left], [node1.right, node2.right])
        }
        return true
    }
}
