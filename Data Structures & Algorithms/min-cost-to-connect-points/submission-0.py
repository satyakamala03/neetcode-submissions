class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1,N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        res = 0
        minH = [[0,0]]
        visit = set()

        while len(visit) < N:
            dist, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += dist
            visit.add(i)
            for neiDist, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiDist, nei])
            
        return res