from pyASEAG.vehicles import vehicles
from pyASEAG.stopPoints import stopPoints
from pyASEAG.journey import journey

import code
import readline
import rlcompleter
import dill
import sys
import time

def help():
    print("TODO: help to implement help()")

def save(filename="lastsession.pkl"):
    dill.dump_session(filename)

def restore(filename="lastsession.pkl"):
    dill.load_session(filename)

def fetcher(stops):
    while True:
        print("Fetching")

        stops.fetchDepartures()


busses = vehicles()
stops = stopPoints(busses)
stops.fetch()
bushof = stops.printFind("Aachen Bushof")
talbot = stops.printFind("Talbot")
hansemann = stops.printFind("Hansemannplatz")
ponttor = stops.printFind("Ponttor")
viktoriaallee = stops.printFind("Viktoriaallee")
elisenbrunnen = stops.printFind("Elisenbrunnen")
normaluhr = stops.printFind("Normaluhr")
ludwig = stops.printFind("Ludwig Forum")
stawag = stops.printFind("STAWAG")

vars = globals()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)
shell.interact(
  banner="Welcome to ASEAG Interactive Shell\n\nType restore() to restore a session or help() for more info\n",
  exitmsg="\nASEAG Interactive Vehicle Shell has been terminated. Your session has been automatically stored in lastsession.pkl"
)
save()
