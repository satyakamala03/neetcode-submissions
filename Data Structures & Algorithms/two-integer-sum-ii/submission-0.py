class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        res = []

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
                while numbers[r] == numbers[r+1] and r > l:
                    r -= 1
            elif curSum < target:
                l += 1
                while numbers[l] == numbers[l-1] and l < r:
                    l += 1
            else:
                return [l + 1,r + 1]
            