class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = defaultdict(list)
        visit = set()
        
        for [c1, c2] in prerequisites:
            courseToPrereq[c1].append(c2)
        
        def dfs(c):
            if c in visit:
                return False
            visit.add(c)
            
            for pre in courseToPrereq[c]:
                if not dfs(pre):
                    return False
                courseToPrereq[c].remove(pre)
            visit.remove(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
