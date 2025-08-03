class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s < target:
                    j += 1
                elif s > target:
                    k -= 1
                if abs(s - target) < abs(ans-target):
                    ans = s
        return ans

        
