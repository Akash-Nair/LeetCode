class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_len = 0
        n = len(s)
        for r in range(n):
            count[s[r]] = count.get(s[r],0) + 1
            curr = r - l + 1
            if curr - max(count.values()) <= k:
                max_len = max(max_len,curr)
            else:
                count[s[l]] -= 1
                l += 1
        return max_len

        
