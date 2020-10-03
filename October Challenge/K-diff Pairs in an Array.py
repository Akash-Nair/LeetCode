class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        ans = set()
        for i in range(len(nums)):
            if nums[i] - k in d:
                ans.add((nums[i]-k,nums[i]))
            if nums[i] + k in d:
                ans.add((nums[i],nums[i]+k))
            d[nums[i]] = i
               
        return len(ans)
        
