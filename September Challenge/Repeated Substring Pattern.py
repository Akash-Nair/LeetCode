class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = ''
        size = len(s)
        for i in range(size-1):
            n += s[i]
            if n*(size//len(n)) == s:
                return True
        return False
        
