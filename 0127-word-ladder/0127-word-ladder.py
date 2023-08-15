class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        
        neighbor = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbor[pattern].append(word)
        
        que = deque([beginWord])
        res = 1
        visited = set()
        
        while que:
            n = len(que)
            for _ in range(n):
                curr = que.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i + 1:]
                    for nei in neighbor[pattern]:
                        if not nei in visited:
                            que.append(nei)
                            visited.add(nei)
            res += 1
        
        return 0
        