from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.ins = defaultdict()
        self.travels = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        first_station,start_time =self.ins[id]
        route = first_station+','+stationName
        if route not in self.travels: 
            self.travels[route]=[0,0]
            
        self.travels[route][0]+=1
        self.travels[route][1]+=t-start_time
            
        
        del self.ins[id] 
    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route2 = startStation+','+endStation
        return self.travels[route2][1]/self.travels[route2][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
