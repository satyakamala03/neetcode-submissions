class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        visit = set()
        queue = deque()
        delta = [[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))
        
        # no rotten oranges in the first place
        if not queue:
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return -1
            return 0
        
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = 2
                    visit.add((nr,nc))
            time += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return time - 1
        

