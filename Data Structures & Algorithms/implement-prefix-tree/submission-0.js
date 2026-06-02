class TrieNode {
    constructor() {
        this.children = new Map()
        this.isWord = false
    }
}

class PrefixTree {
    constructor() {
        this.root = new TrieNode()
    }

    /**
     * @param {string} word
     * @return {void}
     */
    // time - O(len of word), space - O(len of word)
    insert(word) {
        let node = this.root
        for (const letter of word) {
            if (!node.children.has(letter)) node.children.set(letter, new TrieNode())
            node = node.children.get(letter)
        }
        node.isWord = true
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    // time - O(len of word), space - O(1)
    search(word) {
        const node = this.findLastNode(word)
        return node !== null && node.isWord
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    // time - O(len of prefix), space - O(1)
    startsWith(prefix) {
        const node = this.findLastNode(prefix)
        return node !== null
    }

    // time - O(len of word), space - O(1)
    findLastNode(word) {
        let node = this.root
        for (const letter of word) {
            if (!node.children.has(letter)) return null
            node = node.children.get(letter)
        }
        return node
    }
}
