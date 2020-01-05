import requests
from recursive_json import extract_values

def ticketsData(link):
    r = requests.get(link)
    lineNum = extract_values(r.json(), 'LineNumber')
    print(lineNum)

ticketsData('https://www.tpilet.ee/webapi/et/journeys/search?departureStop=tallinn&destinationStop=parnu&departureDate=2020-01-10&returnDate=&price=-1&duration=-1&includeConnections=false&departureBusStopId=17028&destinationBusStopId=8723')