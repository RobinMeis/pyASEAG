class trip:
    def __init__(self):
        self.durationsInSBus = None
        self.durationsInSWalk = None
        self.startStopPoint = None
        self.endStopPoint = None
        self.startDeparture = None
        self.endDeparture = None
        self.parts = None
        self.parentTrip = None
        self.uuid = None
        self.modalType = None

    def setParent(self, parentTrip):
        self.parentTrip = parentTrip

    def addPart(self, newPart):
        if (self.parts == None):
            self.parts = []
        newPart.setParent(self)

        for part in self.parts:
            if part.uuid != None and part.uuid == newPart.uuid:
                return
        self.parts.append(newPart)

    def printTrip(self):
        if self.parts == None:
            print("  %4s %-35s %s %-20s %s %-20s (%s)" % (
                self.startDeparture.lineName,
                self.startDeparture.destinationText,
                self.startDeparture.estimatedTime.strftime('%H:%M:%S'),
                self.startDeparture.stopPoint.stopPointName,
                self.endDeparture.estimatedTime.strftime('%H:%M:%S'),
                self.endDeparture.stopPoint.stopPointName,
                self.startDeparture.vehicleId
            ))
        else:
            print("\n=== %s %s -> %s %s ===" % (
                self.startDeparture.estimatedTime.strftime('%H:%M:%S'),
                self.startStopPoint.stopPointName,
                self.endDeparture.estimatedTime.strftime('%H:%M:%S'),
                self.endStopPoint.stopPointName
            ))
            for part in self.parts:
                part.printTrip()
