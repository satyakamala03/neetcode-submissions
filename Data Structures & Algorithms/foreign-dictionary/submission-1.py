class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c : set() for word in words for c in word} 

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # prefixes equal and len(w1) > len(w2)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        
        visit = set()
        path = set()
        topoSort = []

        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            visit.add(node)
            path.add(node)
            for nb in adjList[node]:
                if not dfs(nb):
                    return False
            topoSort.append(node)
            path.remove(node)
            return True
        
        for c in adjList.keys():
            if not dfs(c):
                return ""
        
        return "".join(topoSort)[::-1]