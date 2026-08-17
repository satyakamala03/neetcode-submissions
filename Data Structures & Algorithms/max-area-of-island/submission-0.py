class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for i in range(ROWS):
            for j in range(COLS):
                area = dfs(i,j)
                max_area = max(max_area, area)
        
        return max_area
