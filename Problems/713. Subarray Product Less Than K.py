class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 1:
            return 0

        curr = 1
        l = 0
        count = 0
        n = len(nums)
        for r in range(n):
            curr *= nums[r]

            while curr >= k:
                curr //= nums[l]
                l += 1

            count += 1 + (r - l)
        return count

        
