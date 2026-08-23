class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)

        ptr = 0
        for i in range(3):
            for j in range(counts[i]):
                nums[ptr] = i
                ptr += 1
        
