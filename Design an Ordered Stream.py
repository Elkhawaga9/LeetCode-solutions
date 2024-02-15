class OrderedStream:
    

    def __init__(self, n: int):
        self.ptr = 0
        self.l1 = [None]*n      

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l1[idKey-1]=value
        if idKey-1==self.ptr: 
            while self.ptr<len(self.l1) and self.l1[self.ptr]!=None:
                self.ptr+=1
            return self.l1[idKey-1:self.ptr]
        else:
            return []

        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
