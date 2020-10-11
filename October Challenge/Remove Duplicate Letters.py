from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        visited = dict()
        stack = []
        
        for char in s:
            visited[char] = False
        
        for char in s:
            c[char] -= 1
            if visited[char]:
                continue
                
            while stack and stack[-1] > char and c[stack[-1]] > 0:
                visited[stack[-1]] = False
                stack.pop()
                
            stack.append(char)
            visited[char] = True
            
            
        
        return ''.join(stack)
        
