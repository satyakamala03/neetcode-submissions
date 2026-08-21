class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        if rows == 0 or cols == 0:
            return 0

        cache = [[-1 for _ in range(cols)] for _ in range(rows)]

        def lcs(r,c):
            if r == rows or c == cols:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            cache[r][c] = max(lcs(r+1,c+1) + (1 if text1[r] == text2[c] else 0), lcs(r+1,c), lcs(r,c+1))
            
            return cache[r][c]
        
        lcs(0,0)
        return cache[0][0]

            
            