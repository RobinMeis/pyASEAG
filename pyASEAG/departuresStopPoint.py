import requests
from .departure import departure

class departuresStopPoint:
    def __init__(self, vehicles, stopPoint):
        self.vehicles = vehicles
        self.stopPoint = stopPoint
        self.departures = {}

    def fetchDepartures(self):
        r = requests.get("http://ivu.aseag.de/interfaces/ura/instant_V1?StopAlso=false&ReturnList=visitnumber,lineid,linename,directionid,destinationtext,destinationname,stoppointindicator,vehicleid,tripid,estimatedtime,expiretime&stopId=%d" % (self.stopPoint.stopPointId,))
        for line in r.text.split("\n"):
            self.parseDeparture(line)

    def addDeparture(self, newDeparture):
        try:
            self.departures[newDeparture.tripId]
        except:
            self.departures[newDeparture.tripId] = newDeparture
            return newDeparture
        else:
            self.departures[newDeparture.tripId].update(newDeparture)
            return self.departures[newDeparture.tripId]

    def parseDeparture(self, departureString):
        newDeparture = departure(self.stopPoint)
        newDeparture.fromString(departureString)
        if (newDeparture.valid):
            self.addDeparture(newDeparture)
            self.vehicles.addDeparture(newDeparture)
            return True
        else:
            return False

    def getDepartures(self):
        departures = sorted(self.departures.values(), key = lambda i: i.estimatedTime)
        return departures

    def getDepature(self, tripId):
        return self.departures[str(tripId)]

    def printDepartures(self):
        print("Departures for %s (%d)\n" % (self.stopPoint.stopPointName, self.stopPoint.stopPointId))
        for e in self.getDepartures():
            print("[%s] %4s %-35s (%s)" % (e.estimatedTime.strftime('%H:%M:%S'), e.lineName, e.destinationName, e.vehicleId))
