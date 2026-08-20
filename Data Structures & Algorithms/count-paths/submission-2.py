class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom-up

        prevRow = [0] * n

        for r in range(m):
            curRow = [0] * n
            curRow[n-1] = 1
            for c in range(n-2, -1, -1):
                curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow
        
        return prevRow[0]