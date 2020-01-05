import requests
from recursive_json import extract_values

def ticketsData(link):
    r = requests.get(link)
    departTime = extract_values(r.json(), 'DepartureDateTime')
    arrivalTime = extract_values(r.json(), 'ArrivalDateTime')
    brandName = extract_values(r.json(), 'BrandName')
    fullPrice = extract_values(r.json(), 'FullPrice')
    salePrice = extract_values(r.json(), 'CampaignPrice')
    print(departTime[0] + '\n')
    print(arrivalTime[0] + '\n')
    print(brandName[0] + '\n')
    print('Полная цена: ' + str(fullPrice[0]) + ' EUR' + '\n')
    print('Цена со скидкой: ' + str(salePrice[0]) + ' EUR' + '\n')

#ticketsData('https://www.tpilet.ee/webapi/et/journeys/search?departureStop=tallinn&destinationStop=parnu&departureDate=2020-01-10&returnDate=&price=-1&duration=-1&includeConnections=false&departureBusStopId=17028&destinationBusStopId=8723')