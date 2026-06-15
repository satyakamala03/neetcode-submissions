class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in numToIndex:
                return sorted([i, numToIndex[req]])
            numToIndex[nums[i]] = i