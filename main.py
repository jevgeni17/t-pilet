from selenium import webdriver
import time
from parse_ticket_data import ticketsData

def main():
    greeting = ('Добро пожаловать в программу покупки билетов! Начнём')
    print(greeting)
    print('Выберите сторону в которую нужны билеты')
    way = {
        1: 'В одну сторону',
        2: 'Туда-обратно',
    }
    for key in way:
        print(key, '->', way[key])

    while True:
        input_ = input(": ")
        if input_ == '1':
            oneWay()     
        elif input_ == '2':
            roundTrip()
        else:
            break

    
def set_options(departure,destination,departureDate,returnDate,returningTrip='0'):
    browser = webdriver.Chrome('/Users/Zeka/Downloads/chromedriver')
    link = ('https://www.tpilet.ee/travel?departureStop=' + departure + '&destinationStop=' + destination + '&departureDate=' + departureDate + '&returnDate=' + returnDate + '&returningTrip=' + returningTrip + '&price=-1&duration=-1')
    browser.get(link)
    
    

    time.sleep(20)
    
def oneWay():
    departure_input = str(input("Укажите город отправления "))
    destination_input = str(input("Укажите город назначения "))
    departure_date_input = str(input("Укажите дату отправления "))
    TALLINN_ID = '17028'
    PARNU_ID = '8723'
    if departure_input == 'parnu':
        link = ('https://www.tpilet.ee/webapi/et/journeys/search?departureStop=parnu&destinationStop=tallinn&departureDate=' + departure_date_input + '&returnDate=&price=-1&duration=-1&includeConnections=false&departureBusStopId=' + PARNU_ID +'&destinationBusStopId=' + TALLINN_ID)
    else:
        link = ('https://www.tpilet.ee/webapi/et/journeys/search?departureStop=tallinn&destinationStop=parnu&departureDate=' + departure_date_input + '&returnDate=&price=-1&duration=-1&includeConnections=false&departureBusStopId=' + TALLINN_ID +'&destinationBusStopId=' + PARNU_ID)

    period_time_input = str(input("Укажите промежуток времени отправления"))
    print("Показать вам ->")
    choose = {
        1: 'Самый дешёвый маршрут',
        2: 'Все маршруты за указ.отрезок времени',
    }
    for key in choose:
        print(key, '->', choose[key])
    while True:
        input_ = input(": ")
        if input_ == '1':
            cheapestTrip(link)     
        elif input_ == '2':
            roundTrip()
        else:
            break
    set_options(departure_input,destination_input,departure_date_input,departure_date_input)

def roundTrip():
    departure_input = str(input("Укажите город отправления "))
    destination_input = str(input("Укажите город назначения "))
    departure_date_input = str(input("Укажите дату отправления "))
    return_date_input = str(input("Укажите дату обратного отправления "))
    set_options(departure_input,destination_input,departure_date_input,return_date_input,returningTrip='1')

def cheapestTrip(link):
    ticketsData(link)

main()