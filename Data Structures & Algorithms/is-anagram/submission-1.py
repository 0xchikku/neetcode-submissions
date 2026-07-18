class Solution:
    # time - O(n), sapce - O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 0
            if t[i] not in counter:
                counter[t[i]] = 0
            counter[s[i]] += 1
            counter[t[i]] -= 1
        
        for value in counter.values():
            if value != 0:
                return False

        return True