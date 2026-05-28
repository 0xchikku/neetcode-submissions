class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    // time - O(n), space - O(n)
    encode(strs) {
        let encodedString = "";
        const marker = "#"
        for(const str of strs) {
            encodedString += str.length + marker + str
        }
        return encodedString;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    // time - O(n), space - O(n)
    decode(str) {
        const decodedStrs = [];
        const marker = "#";
        let i = 0; 
        while (i < str.length) {
            let strlen = 0
            while (str[i] != marker) {
                strlen = (strlen * 10) + parseInt(str[i])
                i++;
            }
            i++; // skip marker
            const decodedStr = str.slice(i, i+strlen)
            i = i+strlen
            decodedStrs.push(decodedStr)
        }
        return decodedStrs
    }
}
