class departuresVehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.departures = {}

    def addDeparture(self, newDeparture):
        try:
            self.departures[newDeparture.tripId]
        except:
            self.departures[newDeparture.tripId] = newDeparture
            return newDeparture
        else:
            self.departures[newDeparture.tripId].update(newDeparture)
            return self.departures[newDeparture.tripId]

    def getDepartures(self):
        departures = sorted(self.departures.values(), key = lambda i: i.estimatedTime)
        return departures

    def printDepartures(self):
        print("Departures for %s\n" % (self.vehicle.vehicleId, ))
        for e in self.getDepartures():
            print("[%s] %4s %-35s (%s)" % (e.estimatedTime.strftime('%H:%M:%S'), e.lineName, e.destinationName, e.stopPoint.stopPointName))
