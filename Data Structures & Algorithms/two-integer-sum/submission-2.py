class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        mpp = {}
        res = []
        for i, a in enumerate(nums):
            b = target - a
            if b in mpp:
                res = [mpp[b], i]
            else:
                mpp[a] = i
        
        return res
