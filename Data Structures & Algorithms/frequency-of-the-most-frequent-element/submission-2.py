class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        L = 0
        res = 1
        
        nums.sort()
        leftSum = 0

        for R in range(len(nums)):
            leftSum += nums[R]
            while (R - L + 1) * nums[R] - leftSum > k:
                leftSum -= nums[L]
                L += 1
            res = max(res, R - L + 1)
        
        return res