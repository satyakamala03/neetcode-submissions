class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n+1)
        
        def dfs(i):
            if i == n or i == n-1:
                dp[i] = 1
                return 1
            if i > n:
                return 0
            if dp[i] is not None:
                return dp[i]
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        
        dfs(0)
        print(dp)
        return dp[0]