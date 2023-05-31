class UndergroundSystem:

    def __init__(self):
        self.check_dict = {}
        self.station_time_dict = defaultdict(int)
        self.station_user = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_dict:
            self.check_dict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_dict:
            start, time = self.check_dict[id]
            self.station_time_dict[(start, stationName)] += (t - time)
            self.station_user[(start), stationName] += 1
            del self.check_dict[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.station_time_dict:
            return self.station_time_dict[(startStation, endStation)] / self.station_user[(startStation, endStation)]
        else:
            return 0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)