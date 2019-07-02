from .vehicle import vehicle

class vehicles:
    def __init__(self):
        self.vehicles = {}

    def getVehicle(self, vehicleId):
        return self.vehicles[str(vehicleId)]

    def addVehicle(self, vehicleId):
        self.vehicles[vehicleId] = vehicle(vehicleId)
        return self.vehicles[vehicleId]

    def addDeparture(self, departure):
        try:
            self.vehicles[departure.vehicleId]
        except KeyError:
            vehicle = self.addVehicle(departure.vehicleId)
        else:
            vehicle = self.vehicles[departure.vehicleId]
        vehicle.addDeparture(departure)
