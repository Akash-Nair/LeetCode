from collections import deque
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        current = 0 
        
        for l,r in sorted(intervals,key = lambda x : (x[0],-x[1])):
            if current < r:
                current = r
                ans += 1
        
        return ans
        
        
        
