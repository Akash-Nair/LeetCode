class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(r*c):
            res.append(matrix[y][x])
            matrix[y][x] = '.'

            if not 0 <= x+dx < c or not 0<= y+dy < r or matrix[y+dy][x+dx] == '.':
                dx, dy = -dy, dx

            x += dx
            y += dy
        return res 
        
