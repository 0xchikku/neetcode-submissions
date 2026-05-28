class Solution {

    // encoder
    inlinePrefixEncoder(strs) {
        let encodedStr = ""
        
        for (const str of strs) {
            const strLen = str.length
            const currentEncodedStr = strLen + '#' + str
            encodedStr += currentEncodedStr
        }

        return encodedStr
    }

    fixedPrefixEncoder(strs) {
        let encodedStr = ""

        for (const str of strs) {
            const strLen = str.length;
            const fixedLengthPrefix = strLen + 1000;
            const currentStrWithPrefix = fixedLengthPrefix + str;
            encodedStr += currentStrWithPrefix;
        }

        return encodedStr;
    }

    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        // return this.inlinePrefixEncoder(strs)
        return this.fixedPrefixEncoder(strs)
    }

    // decoder
    inlinePrefixDecoder(str) {
        let index = 0
        let encodedStrLen = str.length
        const HASH = '#'
        const decodedStr = []
        
        while (index < encodedStrLen) {
            let currentStrLenInString = ''
            while(str[index] !== HASH) {
                currentStrLenInString += str[index]
                index += 1
            }
            const currentStrLenInNum = parseInt(currentStrLenInString)
            index += 1 // to skip HASH
            const currentStr = str.slice(index, index + currentStrLenInNum)
            decodedStr.push(currentStr)
            index = index + currentStrLenInNum
        }

        return decodedStr
    }

    fixedPrefixDecoder(str) {
        const decodedStr = []
        let index = 0
        const encodedStrLen = str.length

        while (index < encodedStrLen) {
            const currentStrLen = parseInt(str.slice(index, index += 4)) - 1000
            const encodedStr = str.slice(index, index += currentStrLen)
            decodedStr.push(encodedStr);
        }

        return decodedStr
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        // return this.inlinePrefixDecoder(str)
        return this.fixedPrefixDecoder(str)
    }
}