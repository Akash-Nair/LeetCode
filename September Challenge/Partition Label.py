class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d ={}
        for i in range(len(S)):
            d[S[i]] = i
            
        start = end = 0
        ans = []
        for i,c in enumerate(S):
            end = max(end,d[c])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans
        
