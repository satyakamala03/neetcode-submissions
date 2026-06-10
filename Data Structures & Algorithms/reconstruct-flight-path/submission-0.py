class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list
        )
        tickets.sort()

        for src, dst in tickets[::-1]:
            adj[src].append(dst)
        
        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        res = res[::-1]
        return res
