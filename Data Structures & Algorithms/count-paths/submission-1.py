class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top-down
        cache = [[0 for _ in range(n)] for _ in range(m)]

        def topDown(r,c):
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n - 1:
                cache[r][c] = 1
                return 1
            cache[r][c] = topDown(r+1,c) + topDown(r,c+1)
            return cache[r][c]
        
        topDown(0,0)
        return cache[0][0]