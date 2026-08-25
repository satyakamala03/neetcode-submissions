class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = 0, 0
        leftBoundary, rightBoundary = [0] * n, [0] * n
        res = 0

        for i in range(n):
            leftBoundary[i] = max(0, leftMax - height[i])
            leftMax = max(leftMax, height[i])
        
        for i in range(n-1, -1, -1):
            rightBoundary[i] = max(0, rightMax - height[i])
            rightMax = max(rightMax, height[i])
        
        for i in range(n):
            res += min(leftBoundary[i], rightBoundary[i])
        
        return res