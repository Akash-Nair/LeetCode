from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d =  defaultdict(int)
        
        for num in nums:
            if num > 0:
                d[num] += 1
                
        if not d:
            return 1
        
        m =  min(d.keys())
        
        if m != 1:
            m = 1
            
        while True:
            if m not in d:
                return m
            m += 1
        
