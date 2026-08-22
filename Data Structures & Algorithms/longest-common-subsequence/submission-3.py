class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        
        if rows == 0 or cols == 0:
            return 0

        dp = [0 for _ in range(cols+1)]

        for r in range(rows-1, -1, -1):
            nextDp = [0 for _ in range(cols+1)]
            for c in range(cols-1, -1, -1):
                nextDp[c] = max(dp[c], nextDp[c+1], dp[c+1] + 1 if text1[r] == text2[c] else 0)            
            dp = nextDp
        
        return dp[0]