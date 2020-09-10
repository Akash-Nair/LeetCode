class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        visited = [0]*len(secret)
        visited_g = [0]*len(guess)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                visited[i] = 1
                visited_g[i] = 1
        
        ans = str(bull) + 'A'
        
        for i in range(len(guess)):
            for j in range(len(secret)):
                if visited[j] == 0 and visited_g[i] == 0:
                    if guess[i] == secret[j]:
                        cow += 1
                        visited[j] = 1
                        visited_g[i] = 1
        ans += str(cow)+'B'
        
        return ans
                
        
