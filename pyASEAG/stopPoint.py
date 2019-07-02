from .departuresStopPoint import departuresStopPoint

class stopPoint:
    def __init__(self, stopPoints, stopPointName, stopPointId, latitude, longitude):
        self.stopPoints = stopPoints
        self.stopPointName = stopPointName
        self.stopPointId = int(stopPointId)
        self.latitude = latitude
        self.longitude = longitude
        self.departures = departuresStopPoint(self.stopPoints.vehicles, self)
        self._globalFetching = False

    def enableGlobalFetching(self):
        self._globalFetching = True

    def disableGlobalFetching(self):
        self._globalFetching = False

    def fetchDepartures(self):
        self.departures.fetchDepartures()

    def print(self):
        print("Information for \"%s\" (%d):\n" % (self.stopPointName, self.stopPointId))
        print("Latitude : %f\nLongitude: %f" % (self.latitude, self.longitude))
        print("Global Fetching: %s" % (self._globalFetching,))

    def getDepartures(self):
        return self.departures.getDepartures()

    def getDeparture(self, tripId):
        return self.departures.getDepature(tripId)

    def printDepartures(self):
        self.departures.printDepartures()

    def addDeparture(self, newDeparture):
        return self.departures.addDeparture(newDeparture)
