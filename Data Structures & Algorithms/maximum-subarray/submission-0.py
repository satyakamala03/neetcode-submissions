class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(0, curSum) # carry forward +ve sum only
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum