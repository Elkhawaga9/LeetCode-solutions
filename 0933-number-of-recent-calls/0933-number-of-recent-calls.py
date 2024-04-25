class RecentCounter:

    def __init__(self):
        self.Counter =deque() 

    def ping(self, t: int) -> int:
        self.Counter.append(t)
        while t > 3000+self.Counter[0]:
            self.Counter.popleft()
        return len(self.Counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)