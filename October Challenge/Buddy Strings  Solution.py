from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        c = Counter(A)
        d = Counter(B)
        possible = 0
        
        if A == B:
            for char in c:
                if c[char] > 1:
                    possible += 1
        
            if possible > 0:
                return True
            else:
                return False
        else:
            if c == d:
                for i in range(len(A)):
                    if A[i] != B[i]:
                        possible += 1

                if possible == 2:
                    return True
                else:
                    return False
            else:
                return False
