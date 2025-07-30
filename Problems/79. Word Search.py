class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(i,j,k):
            if k == len(word):
                return True
            
            if (i < 0 or i >= m) or (j < 0 or j >= n) or word[k] != board[i][j] or (i,j) in visited:
                return False

            visited.add((i,j))
            ans = (dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1))
            visited.remove((i,j))
            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
            
            
