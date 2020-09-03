from sortedcontainers import SortedList
from bisect import bisect_left,bisect_right
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        l = SortedList()
        
        for i in range(len(nums)):
            if i > k:
                l.remove(nums[i-k-1])
            p1 = bisect_left(l,nums[i]-t)
            p2 = bisect_right(l,nums[i]+t)
            
            if p1 != p2 and p1 != len(l):
                return True
            l.add(nums[i])
            
        return False
        
