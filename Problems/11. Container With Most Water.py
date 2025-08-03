class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = -float('inf')
        while l <= r:
            base = r - l
            high = min(height[l],height[r])
            if base*high > ans:
                ans = base*high
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
        
