from selenium import webdriver
import time

while True:
        input_ = input(": ")
        if input_ == '1':
            departure_input = str(input("Укажите город отправления "))
            destination_input = str(input("Укажите город назначения "))
            departure_date_input = str(input("Укажите дату отправления "))
            set_options(departure_input,destination_input,departure_date_input,departure_date_input)
        elif input_ == '2':
            departure_input = str(input("Укажите город отправления "))
            destination_input = str(input("Укажите город назначения "))
            departure_date_input = str(input("Укажите дату отправления "))
            return_date_input = str(input("Укажите дату обратного отправления "))
            set_options(departure_input,destination_input,departure_date_input,return_date_input,returningTrip='1')
            #TODO: website search method here
        else:
            break

    
def set_options(departure,destination,departureDate,returnDate,returningTrip='0'):
    browser = webdriver.Chrome('/Users/Zeka/Downloads/chromedriver')
    browser.get('https://www.tpilet.ee/travel?departureStop=' + departure + '&destinationStop=' + destination + '&departureDate=' + departureDate + '&returnDate=' + returnDate + '&returningTrip=' + returningTrip + '&price=-1&duration=-1')
    
    time.sleep(20)