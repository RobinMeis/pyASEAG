from .departuresStopPoint import departuresStopPoint

class stopPoint:
    def __init__(self, stopPoints, stopPointName, stopPointId, latitude, longitude):
        self.stopPoints = stopPoints
        self.stopPointName = stopPointName
        self.stopPointId = int(stopPointId)
        self.latitude = latitude
        self.longitude = longitude
        self.departures = departuresStopPoint(self.stopPoints.vehicles, self)

    def print(self):
        print("Information for \"%s\" (%d):\n" % (self.stopPointName, self.stopPointId))
        print("Latitude : %f\nLongitude: %f" % (self.latitude, self.longitude))

    def getDepartures(self):
        return self.departures.getDepartures()

    def getDeparture(self, tripId):
        return self.departures.getDepature(tripId)

    def printDepartures(self):
        self.departures.printDepartures()

    def addDeparture(self, newDeparture):
        return self.departures.addDeparture(newDeparture)

    def parseDepartures(self, departureString):
        return self.departures.parseDeparture(departureString)
