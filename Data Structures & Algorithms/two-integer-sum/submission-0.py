class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            b = target - nums[i]
            if b in indices:
                return sorted([i, indices[b]])
            else:
                indices[nums[i]] = i
        