class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        max_len = 0
        l = 0
        n = len(s)
        for r in range(n):
            curr = s[r]
            l = max(l,visited.get(curr,0))
            max_len = max(max_len,r-l+1)
            visited[curr] = r + 1
        return max_len


        
