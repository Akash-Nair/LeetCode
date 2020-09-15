from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l = [1,2,3,4,5,6,7,8,9]
        c = combinations(l,k)
        
        ans = []
        for comb in c:
            if sum(comb) == n:
                ans.append(comb)
                
        return ans
