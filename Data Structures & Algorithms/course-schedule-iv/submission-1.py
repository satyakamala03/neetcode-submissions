class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        indirectPrereqs = [None] * numCourses

        # we are given [pre, crs]
        for i in range(numCourses):
            adjList[i] = []

        for pre, crs in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(node):
            if indirectPrereqs[node] is not None:
                return indirectPrereqs[node]

            pres = set()
            for nb in adjList[node]:
                pres.add(nb)
                pres.update(dfs(nb))
            indirectPrereqs[node] = pres
            return pres
        
        for i in range(numCourses):
            dfs(i)
            
        print(indirectPrereqs)
        answer = []
        for u, v in queries:
            answer.append(True if u in indirectPrereqs[v] else False)
        
        return answer

        
        


        