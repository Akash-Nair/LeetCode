class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(remain, combo, index):
            if remain == 0:
                result.append(combo)
                return
            for i in range(index, len(candy)):
                if candy[i] > remain:
                    break 
                dfs(remain - candy[i], combo + [candy[i]], i)
                
        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result
            
