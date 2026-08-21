class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        
        cache = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        cache[ROWS-1][COLS-1] = 1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    cache[r][c] = 1
                elif r + 1 < ROWS and c + 1 < COLS and obstacleGrid[r][c] == 0:
                    cache[r][c]+= cache[r + 1][c] + cache[r][c+1]
                elif r + 1 == ROWS and obstacleGrid[r][c] == 0:
                    cache[r][c] += cache[r][c+1]
                elif c + 1 == COLS and obstacleGrid[r][c] == 0:
                    cache[r][c] += cache[r+1][c]
                elif obstacleGrid[r][c] == 1:
                    cache[r][c] = 0
        print(cache)
        return cache[0][0]