from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = defaultdict(int)
        dt = defaultdict(int)
        
        for letter in s:
            ds[letter] += 1
            
        for letter in t:
            dt[letter] += 1
            
        for letter in dt:
            if dt[letter] != ds[letter]:
                return letter
        
        
        
