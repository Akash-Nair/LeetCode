from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int
                       )
        for i in range(len(s)-10+1):
            d[s[i:i+10]] += 1
            
            
        answer = []    
        for i in d:
            if d[i] > 1:
                answer.append(i)
                
        return answer
            
        
        
