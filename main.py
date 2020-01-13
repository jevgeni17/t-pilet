from selenium import webdriver
import time
from recursive_json import extract_values
import requests
import re
from termcolor import colored

def main():
    """main function"""

    global browser
    browser = webdriver.Chrome('/Users/Zeka/Downloads/chromedriver')
    greeting = ('Добро пожаловать в программу покупки билетов! Начнём')
    print(greeting)
    print('Выберите маршрут')
    way = {
        1: 'tallinn-parnu'
    }
    for key in way:
        print(key, '->', way[key])
    while True:
        input_ = input(": ")
        if input_ == '1':
            get_journeys()
        #elif input_ == '2':
        #    roundTrip()
        else:
            break

def options(departureDate,departure='tallinn',destination='parnu',returningTrip='0'):
    """function that creates a link for the trip 'tallinn' -> 'parnu' and passes it to the browser"""

    link = ('https://www.tpilet.ee/travel?departureStop=' + departure + '&destinationStop=' + destination + '&departureDate=' + departureDate + '&returnDate=' + departureDate + '&returningTrip=' + returningTrip + '&price=-1&duration=-1')
    browser.get(link) 
    time.sleep(5)


def get_journeys():
    """function that do main work """

    departure_date = str(input("Укажите дату отправления "))
    options(departure_date)

    js_times="""
    var times = document.getElementsByClassName('vqA6QljR2KNt8yw9PHk9C');
    let time = [];
    for (var i = 0; i < times.length; i++){time.push( 
    times[i].innerText);console.log(time);} return time;
    """

    js_company="""
    var company = document.getElementsByClassName('lvCBxuihqm3iUoMcebtd4');
    let companys = [];
    for (var i = 0; i < company.length; i++){companys.push( 
    company[i].innerText);console.log(companys);} return companys;
    """
    
    js_tickets="""
    var ticket = document.getElementsByClassName('_3TJaMCIiSE5gyvUGhXPJ_f');
    let tickets = [];
    for (var i = 0; i < ticket.length; i++){tickets.push( 
    ticket[i].innerText);console.log(tickets);} return tickets;
    """

    js_seats="""
    var seat = document.getElementsByClassName('_1bELoiN2P2KjAtnIfRarX-');
    let seats = [];
    for (var i = 0; i < seat.length; i++){seats.push( 
    seat[i].innerText);console.log(seats);} return seats;
    """

    """Scrap some data from tpilet """

    times = browser.execute_script(js_times)
    company = browser.execute_script(js_company)
    ticket = browser.execute_script(js_tickets)
    seat = browser.execute_script(js_seats)
    

    TALLINN_ID = '17028'
    PARNU_ID = '8723'

    """link to get json web-api"""

    link = ('https://www.tpilet.ee/webapi/et/journeys/search?departureStop=tallinn&destinationStop=parnu&departureDate=' + departure_date + '&returnDate=&price=-1&duration=-1&includeConnections=false&departureBusStopId=' + TALLINN_ID +'&destinationBusStopId=' + PARNU_ID)
    r = requests.get(link)

    """Scrap some data from json web-api"""

    fullPrice = extract_values(r.json(), 'FullPrice')
    salePrice = extract_values(r.json(), 'CampaignPrice')
    tripId = extract_values(r.json(), 'TripId')
    DEP_ID = extract_values(r.json(), 'DepartureRouteStopId')
    DEST_ID = extract_values(r.json(), 'DestinationRouteStopId')

    """Convert lists to dictionaries"""

    times_dict = { i : times[i] for i in range(0, len(times) ) }
    company_dict = { i : company[i] for i in range(0, len(company) ) }
    full_dict = { i : fullPrice[i] for i in range(0, len(fullPrice) ) }
    sale_dict = { i : salePrice[i] for i in range(0, len(salePrice) ) }
    

    for key in times_dict and company_dict and full_dict and sale_dict:
        print(key, '--->>>', times_dict[key], '   ', company[key], '    ПОЛНАЯ ЦЕНА',fullPrice[key],'    СО СКИДКОЙ',salePrice[key],)  

    num = int(input())
    num+-1
    """link to get json web-api"""

    linkk = ('https://www.tpilet.ee/webapi/et/trips/prices?tripId='+ str(tripId[num])+ '&departureRouteStopId='+str(DEP_ID[num])+'&destinationRouteStopId='+str(DEST_ID[num]))
    rr = requests.get(linkk)

    time.sleep(3)
    q = browser.execute_script("document.getElementsByClassName('OxitbZN0S38kKLBZlAssO')[" + str(num) +"].click()")
    time.sleep(2)

    q = [re.sub(r'\n', ' ', i) for i in ticket]
    newtest = [x[:-1] for x in q] 
    #print(newtest)
    tickets_dict = { i : newtest[i] for i in range(0, len(newtest) ) }

    for key in tickets_dict:
        print(key, '--->>>', tickets_dict[key])

    inp = str(input())

    q = browser.execute_script("document.getElementsByClassName('_3mbZTemfn3cnxwKkLHZs-m')[" + str(inp) +"].click()")
    time.sleep(3)
    
    w = [re.sub(r'\n', ' ', i) for i in seat]
    #print(w)


    a = [['1', '2', '3', '4'], ['5', '6', '7', '8'], # list of all seats
        ['9', '10','11', '12'], ['13', '14', '15', '16'],
         ['17', '18', '19', '20'], ['21', '22', '23', '24'],
          ['25', '26', '27', '28'], ['29', '30','31','32'],
                                    ['33','34','35','36']]
    a = sum(a, [])
    result = []
    for elem in a:
        if not str(elem).isdigit():
            continue
        if elem in w:
            result.append((colored(elem, 'green'))) # available seats
        else:
            result.append((colored(elem, 'red'))) # occupied seats

        if len(result) % 4 == 0:
            print('  '.join(result))
            result = []

    inpp = input()
    q = browser.execute_script("document.getElementById('web-tickets-busseat-" + inpp +"').click()")
    time.sleep(100)

if __name__ == "__main__":
    main()