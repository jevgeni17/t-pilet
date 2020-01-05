from selenium import webdriver
import time

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
    
    
    
    #elem = browser.find_element_by_name('Lähtepeatus')
    #elem.click()
    #elem.send_keys('232')
    
    
main()