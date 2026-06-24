class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # build adjacency list
        adjList = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adjList[pattern].append(word)
        
        # bfs to find shortest path 
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in adjList[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)

            res += 1
        
        return 0
        
