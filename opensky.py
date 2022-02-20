import requests
class opensky:
    
    def __init__(self) -> None:
        pass
    
    def getRawData(icao24, t=0):
        if t == 0: statevectors = requests.get("https://opensky-network.org/api/states/all?icao24=" + icao24.casefold())
        else: statevectors = requests.get("https://opensky-network.org/api/states/all?icao24=" + icao24.casefold() + "&time=" + str(t))
        return statevectors.json()
    
    