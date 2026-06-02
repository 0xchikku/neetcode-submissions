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
    // time - O(len of word), space - O(len of word)
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
    // time - O(26^(len of word)), space - O(len of word)
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
