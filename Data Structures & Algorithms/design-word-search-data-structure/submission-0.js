class TrieNode {
    constructor() {
        this.children = new Map()
        this.isWord = false
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode()
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
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
    search(word) {
        const recursion = (index, node) => {
            for (let i = index; i < word.length; i++) {
                const letter = word[i]
                if (letter === ".") {
                    for (const child of node.children.values()) {
                        if (recursion(i+1, child)) return true
                    }
                    return false
                } else {
                    if (!node.children.has(letter)) return false
                    node = node.children.get(letter)
                }
            }
            return node.isWord
        }
        return recursion(0, this.root)
    }
}
