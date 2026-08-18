class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        path = set()
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []
        
        for src, dest in prerequisites:
            adjList[src].append(dest)
        
        def topoSort(node):
            if node in path:
                return False
            if node in visit:
                return True
            visit.add(node)
            path.add(node)
            for nb in adjList[node]:
                if not topoSort(nb):
                    return False
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if not topoSort(i):
                return False
        
        return True
