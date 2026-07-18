class Solution:
    # time - O(n*m), space - O(n*m) - n - len of strs, m - avg len of str
    def encode(self, strs: List[str]) -> str:
        encodedStrs = []
        marker = "#"

        for string in strs:
            encoded = str(len(string)) + marker + string
            encodedStrs.append(encoded)

        return "".join(encodedStrs)

    # time - O(n), space - O(n) - n - len of str, m - avg len of str
    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        marker = "#"

        i = 0
        while i < len(s):
            length = 0
            while i < len(s) and s[i] != marker:
                length = (length * 10) + int(s[i])
                i += 1

            i += 1

            string = s[i : i + length]
            decodedStrs.append(string)

            i = i + length

        return decodedStrs
