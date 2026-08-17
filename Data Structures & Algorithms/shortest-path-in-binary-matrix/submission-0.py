class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        # 8 directional connection
        delta = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        length = 1

        queue.append((0,0))
        visit.add((0,0))

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    queue.append((nr,nc))
                    visit.add((nr,nc))
            length += 1
        
        return -1

