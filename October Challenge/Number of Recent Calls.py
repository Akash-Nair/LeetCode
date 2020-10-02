class RecentCounter:

    def __init__(self):
        self.data = []
        self.last = 0
        

    def ping(self, t: int) -> int:
        self.data.append(t)
        cnt = 0
        for i in range(len(self.data)-self.last-1,len(self.data)):
            if t - 3000 <= self.data[i] <= t:
                cnt+=1
        self.last = cnt
        return cnt
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
