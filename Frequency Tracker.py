from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.valid = defaultdict(int)

    def add(self, number: int) -> None:
        if self.valid[self.freq[number]]>0: 
            self.valid[self.freq[number]]-=1
        self.freq[number] += 1
        self.valid[self.freq[number]]+=1
        
    def deleteOne(self, number: int) -> None:
        if self.freq[number]>0:
            self.valid[self.freq[number]]-=1
            self.freq[number]-=1
            self.valid[self.freq[number]]+=1

        
    def hasFrequency(self, frequency: int) -> bool:
        if self.valid[frequency]>0:
            return True
        return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
