class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encodedStr = ""
        const separator = '#'
        
        for (const currentStr of strs) {
            const currentStrLen = currentStr.length
            const currentEncodedStr = [currentStrLen, separator, currentStr].join("")
            encodedStr += currentEncodedStr
        }

        return encodedStr
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let index = 0
        let encodedStrLen = str.length
        const separator = '#'
        const decodedStr = []
        
        while (index < encodedStrLen) {
            let currentStrLenInString = ''
            while(str[index] !== separator) {
                currentStrLenInString += str[index]
                index += 1
            }
            const currentStrLenInNum = parseInt(currentStrLenInString)
            index += 1 // to skip separator
            const currentStr = str.slice(index, index + currentStrLenInNum)
            decodedStr.push(currentStr)
            index = index + currentStrLenInNum
        }

        return decodedStr
    }
}