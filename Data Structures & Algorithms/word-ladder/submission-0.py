class Solution:
    # time - O((m ^ 2) * n), space - O((m ^ 2) * n)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        patternMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patternMap[pattern].append(word)
        
        visit = set([beginWord])
        queue = deque([beginWord])
        length = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nextWord in patternMap[pattern]:
                        if nextWord not in visit:
                            visit.add(nextWord)
                            queue.append(nextWord)
                    patternMap[pattern] = []
            length += 1
        return 0
                