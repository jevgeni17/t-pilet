import requests
from recursive_json import extract_values
from itertools import groupby

def ticketsData(link):
    r = requests.get(link)
    departTime = extract_values(r.json(), 'DepartureDateTime')
    arrivalTime = extract_values(r.json(), 'ArrivalDateTime')
    brandName = extract_values(r.json(), 'BrandName')
    fullPrice = extract_values(r.json(), 'FullPrice')
    salePrice = extract_values(r.json(), 'CampaignPrice')
    new_depart = [el for el, _ in groupby(departTime)]
    new_arrival = [el for el, _ in groupby(arrivalTime)]
    #print(str(new_depart) + '\n')  # NB <---- depart and arrival ALWAYS needs *2
    #print(str(new_arrival) + '\n')
    #print(str(brandName) + '\n')
    #print('Полная цена: ' + str(fullPrice) + ' EUR' + '\n')
    #print('Цена со скидкой: ' + str(salePrice) + ' EUR' + '\n')
    #q = min(filter(None, salePrice))
    #newlist = enumerate(salePrice)
    #for index, item in newlist:
    #    if item == q:
            #print(index, item)
    matching = [s for s in departTime if '10:00' in s]
    matching_new = enumerate(matching)
    for index, item in matching_new:
        print(index, item)
ticketsData('https://www.tpilet.ee/webapi/et/journeys/search?departureStop=tallinn&destinationStop=parnu&departureDate=2020-01-09&returnDate=&includeConnections=false&departureBusStopId=17028&destinationBusStopId=8723')