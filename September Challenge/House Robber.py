class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            temp = [0]*n
            m = nums[0]
            temp[0] = m
            
            if nums[1] > temp[0]:
                m = nums[1]
            
            temp[1] = m
            
            for i in range(2,n):
                x = max(m,nums[i],temp[i-2]+nums[i])
                temp[i] = x
                if x > m:
                    m = x
                    
            return temp[-1]
        
