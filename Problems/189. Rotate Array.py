class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0
        i = 0
    
        while count < n:
            curr,prev = i,nums[i]
            while True:
                nex = (curr + k)%n
                nums[nex],prev = prev,nums[nex]
                curr = nex
                count += 1
                if i == curr:
                    break
                
            i += 1
