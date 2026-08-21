class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}

        def backtrack(i, curSum):
            if i == n and curSum == target:
                return 1
            if i == n:
                return 0
            if (i,curSum) in cache.keys():
                return cache[(i,curSum)]
            cache[(i,curSum)] = backtrack(i+1, curSum + nums[i]) + backtrack(i+1, curSum - nums[i])
            return cache[(i,curSum)]
        
    
        return backtrack(0,0)