from collections import defaultdict
class Solution:
    def check(self,x):
        temp = []
        for i in range(len(x)):
            for j in range(len(x)):
                if x[i][j] == 1:
                    temp.append((i,j))
        return temp
    
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        ans = 0
        d = defaultdict(int)
        
        a = self.check(A)
        b = self.check(B)
        
        for (x1,y1) in a:
            for (x2,y2) in b:
                vec = (x1-x2,y1-y2)
                d[vec] += 1
                ans = max(ans,d[vec])
        return ans
        
