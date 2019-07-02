import datetime

class departure:
    def __init__(self, stopPoint):
        self.stopPoint = stopPoint

    def update(self, newDeparture):
        if newDeparture.valid:
            self.stopPointIndicator = newDeparture.stopPointIndicator
            self.visitNumber = newDeparture.visitNumber
            self.lineId = newDeparture.lineId
            self.lineName = newDeparture.lineName
            self.directionId = newDeparture.directionId
            self.destinationText = newDeparture.destinationText
            self.destinationName = newDeparture.destinationName
            self.vehicleId = newDeparture.vehicleId
            self.tripId = newDeparture.tripId
            self.estimatedTime = newDeparture.estimatedTime
            self.expireTime = newDeparture.expireTime
            self.valid = True

    def fromString(self, departureString):
        self.valid = False
        self.departureString = departureString
        self.departure = json.loads(departureString)
        if (len(self.departure) != 12):
            return

        self.unknown = self.departure[0]
        self.stopPointIndicator = self.departure[1]
        self.visitNumber = self.departure[2]
        self.lineId = self.departure[3]
        self.lineName = self.departure[4]
        self.directionId = self.departure[5]
        self.destinationText = self.departure[6]
        self.destinationName = self.departure[7]
        self.vehicleId = self.departure[8]
        self.tripId = self.departure[9]
        self.estimatedTime = datetime.datetime.fromtimestamp(self.departure[10]/1000)
        self.expireTime = datetime.datetime.fromtimestamp(self.departure[11]/1000)
        self.valid = True
