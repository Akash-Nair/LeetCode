from collections import deque
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        p1 = deque()
        id1 = 0
        p2 = deque()
        id2 = 0
        
        for c in pattern:
            if c in d:
                p1.append(d[c])
            else:
                d[c] = id1
                p1.append(d[c])
                id1 += 1
        d = {}      
        for word in str.split():
            if word in d:
                p2.append(d[word])
            else:
                d[word] = id2
                p2.append(d[word])
                id2 += 1
        
        return p1 == p2
        
        
        
