class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        visit = set()
        prev = -1

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(node, prev):
            if node in visit:
                return False
            # if adjList[node] == []: # no loop encountered so far
            #     return True
            
            visit.add(node)
            for c in adjList[node]:
                if c == prev:
                    continue
                if not dfs(c,node):
                    return False
            return True
        
        if not dfs(0, -1) or len(visit) != n:
            return False
        else: 
            return True
                


