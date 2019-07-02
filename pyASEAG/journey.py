import datetime
import requests
import json
from .trip import trip
from .departure import departure

class journey:
    def __init__(self, startStop=None, endStop=None, departureTime=None):
        if (startStop.stopPoints != endStop.stopPoints):
            raise Exception("startStop and endStop have to be member of the same stopPoint object")
        self.stopPoints = startStop.stopPoints
        self.startStop = startStop
        self.endStop = endStop
        self.departureTime = departureTime
        self.trips = {}
        self.maxDuration = None

    def printJourney(self):
        for trip in self.trips:
            self.trips[trip].printTrip()

    def getStartStop(self):
        return self.startStop

    def setStartStop(self, startStop):
        self.startStop = startStop

    def getEndStop(self):
        return self.endStop

    def setStartStop(self):
        self.endStop = endStop

    def getDepatureTime(self):
        return self.departureTime

    def setDepartureTime(self, departureTime):
        self.departureTime = departureTime

    def fetch(self):
        if (self.startStop == None or self.endStop == None):
            raise Exception("startStop and endStop have to be set")

        if (self.departureTime == None):
            departureTime = datetime.datetime.now()
        else:
            departureTime = self.departureTime

        r = requests.get("http://ivu.aseag.de/interfaces/ura/journey?departureTime=%d&startStopId=%d&maxNumResults=10&endStopId=%d" %
            (int(datetime.datetime.timestamp(departureTime)*1000),
            self.startStop.stopPointId,
            self.endStop.stopPointId
            )
        )
        results = json.loads(r.text)
        self.maxDuration = results["maxJourneyDurationInS"]
        for result in results["resultList"]:
            try:
                curTrip = self.trips[result["uuid"]]
            except KeyError:
                self.trips[result["uuid"]] = trip()
                curTrip = self.trips[result["uuid"]]

            try:
                curTrip.durationsInSBus = result["durationsInS"]["bus"]
            except KeyError:
                print("Why doesn't ASEAG provide a Bus connection when I ask them?")
                continue
            curTrip.startStopPoint = self.stopPoints.getStop(result["startLocation"]["stopPointId"])
            curTrip.endStopPoint = self.stopPoints.getStop(result["endLocation"]["stopPointId"])
            curTrip.durationsInSWalk = result["durationsInS"]["walk"]
            curTrip.uuid = result["uuid"]

            for change in result["elementList"]:
                if change["modalType"] == "walk":
                    print("I didn't ask ASEAG because I desired to walk!")
                    continue
                part = trip()
                part.setParent(curTrip)
                part.startStopPoint = self.stopPoints.getStop(change["start"]["location"]["stopPointId"])
                part.endStopPoint = self.stopPoints.getStop(change["end"]["location"]["stopPointId"])
                part.uuid = change["uuid"]
                part.modalType = change["modalType"]

                newDeparture = departure(part.startStopPoint)
                newDeparture.stopPointIndicator = change["start"]["location"]["stopPointIndicator"]
                newDeparture.visitNumber = change["start"]["visitNumber"]
                newDeparture.lineId = change["lineId"]
                newDeparture.lineName = change["lineName"]
                newDeparture.directionId = None
                newDeparture.destinationText = change["destinationText"]
                newDeparture.destinationName = change["destinationName"]
                try:
                    newDeparture.vehicleId = change["vehicleId"]
                except KeyError:
                    newDeparture.vehicleId = None
                newDeparture.tripId = change["tripId"]
                if change["start"]["estimatedDepartureInUnixEpochMillis"] != 0:
                    departureTime = change["start"]["estimatedDepartureInUnixEpochMillis"]
                else:
                    departureTime = change["start"]["scheduledDepartureInUnixEpochMillis"]
                newDeparture.estimatedTime = datetime.datetime.fromtimestamp(departureTime/1000)
                newDeparture.expireTime = datetime.datetime.fromtimestamp(departureTime/1000)
                newDeparture.valid = True
                part.startDeparture = part.startStopPoint.addDeparture(newDeparture)
                part.startStopPoint.stopPoints.vehicles.addDeparture(newDeparture)

                newDeparture = departure(part.endStopPoint)
                newDeparture.stopPointIndicator = change["end"]["location"]["stopPointIndicator"]
                newDeparture.visitNumber = change["end"]["visitNumber"]
                newDeparture.lineId = change["lineId"]
                newDeparture.lineName = change["lineName"]
                newDeparture.directionId = None
                newDeparture.destinationText = change["destinationText"]
                newDeparture.destinationName = change["destinationName"]
                try:
                    newDeparture.vehicleId = change["vehicleId"]
                except KeyError:
                    newDeparture.vehicleId = None
                newDeparture.tripId = change["tripId"]
                if change["end"]["estimatedDepartureInUnixEpochMillis"] != 0:
                    departureTime = change["end"]["estimatedDepartureInUnixEpochMillis"]
                else:
                    departureTime = change["end"]["scheduledDepartureInUnixEpochMillis"]
                newDeparture.estimatedTime = datetime.datetime.fromtimestamp(departureTime/1000)
                newDeparture.expireTime = datetime.datetime.fromtimestamp(departureTime/1000)
                newDeparture.valid = True
                part.endDeparture = part.endStopPoint.addDeparture(newDeparture)
                part.endStopPoint.stopPoints.vehicles.addDeparture(newDeparture)
                curTrip.addPart(part)

            curTrip.startDeparture = curTrip.parts[0].startDeparture
            curTrip.endDeparture = part.endDeparture
