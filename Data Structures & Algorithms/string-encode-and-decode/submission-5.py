class Solution:

    def encode(self, strs: List[str]) -> str:
        decoded = []
        marker = "#"
        for word in strs:
            val = str(len(word)) + marker + word
            decoded.append(val)
        
        return "".join(decoded)


    def decode(self, s: str) -> List[str]:
        res = []
        marker = "#"
        i = 0
        while i < len(s):
            strLen = 0
            while i < len(s) and s[i] != marker:
                strLen = (strLen * 10) + int(s[i])
                i += 1
            i += 1
            if strLen == 0:
                word = ""
            else:
                word = s[i: i+strLen]
            res.append(word)
            i = i + strLen
        return res

