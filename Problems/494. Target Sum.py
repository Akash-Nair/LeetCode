class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index,total):
            key = (index,total)
            if key not in visited:
                if index == len(nums):
                    return 1 if total == target else 0
                else:
                    visited[key] = dfs(index+1,total+nums[index]) + dfs(index+1,total-nums[index])
            return visited[key]
        visited = defaultdict(int)
        return dfs(0,0)
