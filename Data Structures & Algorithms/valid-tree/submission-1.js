class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        const adjList = new Map()
        for (let i = 0; i < n; i++) {
            adjList.set(i, [])
        }

        for (let edge of edges) {
            const [node1, node2] = edge
            adjList.get(node1).push(node2)
            adjList.get(node2).push(node1)
        }

        const visited = new Set()
        const checked = new Set()

        const hasCycle = (node, prevParent) => {
            if (checked.has(node)) return false
            if (visited.has(node)) return true

            visited.add(node)
            for (let child of adjList.get(node)) {
                if (child === prevParent) continue // skipping parent node
                if (hasCycle(child, node)) return true
            }
            visited.delete(node)
            checked.add(node)
            return false
        }

        if (hasCycle(0, -1)) return false
        if (checked.size !== n) return false
        return true
    }
}
