class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(row, col, grid):
            # base case
            if (row, col) in visit:
                return

            # otherwise
            visit.add((row,col))

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[row][col]:
                    grid[r][c] = True
                    dfs(row + dr, col + dc, grid)
        

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific[i][j] = True
        
        for i in range(m):
            for j in range(n):
                if i == m-1 or j == n-1:
                    atlantic[i][j] = True
                    
        
        visit = set()
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == True:
                    dfs(i, j, pacific)

        visit = set()
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] == True:
                    dfs(i, j, atlantic)
        
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == True and atlantic[i][j] == True:
                    res.append([i,j])
        
        return res

