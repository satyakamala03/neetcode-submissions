class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        i = j = 0
        dp = {}

        def dfs(i, j):
            # base case
            if j == len(t):
                dp[(i,j)] = 1
                return 1
            if i == len(s):
                dp[(i,j)] = 0
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            # choices
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1, j+1) + dfs(i+1,j)
            else:
                dp[(i,j)] = dfs(i+1, j)
            return dp[(i,j)]
        
        return dfs(0,0)