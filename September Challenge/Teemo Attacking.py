class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        if not timeSeries:
            return 0
        elif len(timeSeries) == 1:
            return duration
        else:
            for i in range(len(timeSeries)-1):
                if timeSeries[i+1] < timeSeries[i] + duration:
                    total +=  timeSeries[i+1] - timeSeries[i]
                else:
                    total += duration
            total += duration
            
        return total
        
        
