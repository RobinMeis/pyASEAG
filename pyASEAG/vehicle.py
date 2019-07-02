from .departuresVehicle import departuresVehicle

class vehicle:
    def __init__(self, vehicleId):
        self.vehicleId = vehicleId
        self.departures = departuresVehicle(self)

    def addDeparture(self, departure):
        self.departures.addDeparture(departure)

    def getDepartures(self):
        return self.departures.getDepartures()

    def printDepartures(self):
        self.departures.printDepartures()
