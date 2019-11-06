import requests
import json
from .stopPoint import stopPoint

class stopPoints:
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.stopPoints = {}

    def fetch(self):
        r = requests.get("http://ivu.aseag.de/interfaces/ura/location?searchString=*&maxResults=10000")
        stopPoints = json.loads(r.text)
        for point in stopPoints["resultList"]:
            if (point["type"] == "StopPoint"):
                self.stopPoints[str(point["stopPointId"])] = stopPoint(
                                                            self,
                                                            point["stopPointName"],
                                                            point["stopPointId"],
                                                            point["latitude"],
                                                            point["longitude"]
                )

    def fetchDepartures(self):
        r = requests.get("http://ivu.aseag.de/interfaces/ura/instant_V1?StopAlso=false&ReturnList=stopid,visitnumber,lineid,linename,directionid,destinationtext,destinationname,stoppointindicator,vehicleid,tripid,estimatedtime,expiretime")
        r.raise_for_status()
        for departureString in r.text.split("\n"):
            departureLine = json.loads(departureString)
            if (departureLine[0] == 1):
                try:
                    stopPoint = self.getStop(departureLine[1])
                except KeyError:
                    print("Unknown stop found!")
                else:
                    if (not stopPoint.parseDepartures(departureString)):
                        print("Parsing failed for a stop")

    def find(self, string):
        string = string.lower()
        results = []
        for stop in self.stopPoints:
            if (self.stopPoints[stop].stopPointName.lower().find(string) != -1):
                results.append(self.stopPoints[stop])
        return results

    def printFind(self, string):
        results = self.find(string)
        print("Results for %s:" % (string, ))
        for result in results:
            print("%d %s" % (result.stopPointId, result.stopPointName))

        if (len(results) == 1):
            print("\nResult has been returned")
            return results[0]
        else:
            return None

    def getStop(self, stopId):
        return self.stopPoints[str(stopId)]

    def getStopPoints(self):
        return self.stopPoints.values()
