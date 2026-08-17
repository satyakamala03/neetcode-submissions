class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        queue = deque()
        delta = [[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        if not queue:
            return 0 if fresh == 0 else -1
        
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1
        
        return time - 1 if fresh == 0 else -1
        

