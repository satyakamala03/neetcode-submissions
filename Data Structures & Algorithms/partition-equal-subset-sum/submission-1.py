class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        target = total // 2
        ROWS, COLS = len(nums), target + 1
        cache = [[None for _ in range(COLS)] for _ in range(ROWS)]

        def dp(i, rem):
            if rem == 0:
                return True
            if i == ROWS or rem < 0:
                return False
            if cache[i][rem] is not None:
                return cache[i][rem]
            # skip i
            skip = dp(i+1,rem)
            newRem = rem - nums[i]
            take = dp(i+1,rem - nums[i])
            cache[i][rem] = skip or take

            return cache[i][rem]
        
        return dp(0,target)
