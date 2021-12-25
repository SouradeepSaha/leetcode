class UndergroundSystem:

    def __init__(self):
        self.travellers, self.routes = dict(), dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travellers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.travellers[id]
        timeTaken = t - startTime
        route = startStation + "-" + stationName
        
        if route not in self.routes:
            self.routes[route] = [0,0]
        self.routes[route][0] += timeTaken
        self.routes[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = startStation + "-" + endStation
        return self.routes[route][0] / self.routes[route][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
