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
        for stop in self.stopPoints:
            stop = self.stopPoints[stop]
            if (stop._globalFetching):
                stop.fetchDepartures()

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
