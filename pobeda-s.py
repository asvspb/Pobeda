from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import csv

def get_cheapest_tickets(origin, destination, start_date, days):
    cheapest_tickets = []

    # Настройки для Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    origin_city_name = cities[origin_choice]['name']
    destination_city_name = cities[destination_choice]['name']
    print(f"\nИдет поиск билетов {origin_city_name} - {destination_city_name} на {days} дн. вперед...")

    for i in range(days):
        current_date = start_date + timedelta(days=i)
        formatted_date = current_date.strftime('%d.%m.%Y')

        url = f"https://ticket.flypobeda.ru/websky/?origin-city-code[0]={origin}&destination-city-code[0]={destination}&date[0]={formatted_date}&segmentsCount=1&adultsCount=1&youngAdultsCount=0&childrenCount=0&infantsWithSeatCount=0&infantsWithoutSeatCount=0&lang=ru#/search"

        try:
            driver.get(url)
            # Ждем загрузки элементов с ценами
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'price-cell__text'))
            )

            price_elements = driver.find_elements(By.CLASS_NAME, 'price-cell__text')
            prices = [float(price.text.replace('₽', '').replace(' ', '').replace('\xa0', '')) for price in price_elements if price.text]

            if prices:
                min_price = min(prices)
                min_price_index = prices.index(min_price)

                flight_info_element = driver.find_elements(By.CLASS_NAME, 'contentRow')[min_price_index]
                time_element = flight_info_element.find_element(By.CLASS_NAME, 'time')
                departure_time, arrival_time = time_element.text.split(' – ')

                cheapest_tickets.append({
                    'date': formatted_date,
                    'price': min_price,
                    'departure_time': departure_time,
                    'arrival_time': arrival_time
                })

                # Выводим информацию о найденном билете
                print(f"Дата: {formatted_date}, Цена: {min_price}₽, "
                      f"Вылет: {departure_time}, Прилет: {arrival_time}")
            else:
                print(f"Цены на {formatted_date} не найдены.")

        except Exception as e:
            print(f"Не удалось получить данные на {formatted_date}.")

        time.sleep(1)

    driver.quit()
    return cheapest_tickets, origin_city_name, destination_city_name

if __name__ == "__main__":
    # Города и их коды IATA
    cities = {
        '1': {'name': 'Санкт-Петербург', 'code': 'LED'},
        '2': {'name': 'Волгоград', 'code': 'VOG'},
        '3': {'name': 'Москва', 'code': 'MOW'},
        '4': {'name': 'Саратов', 'code': 'RTW'},
        '5': {'name': 'Калининград', 'code': 'KGD'},
        '6': {'name': 'Краснодар', 'code': 'KRR'},
        '7': {'name': 'Сочи', 'code': 'AER'},
        '8': {'name': 'Омск', 'code': 'OMS'},
        '9': {'name': 'Абу-Даби', 'code': 'AUH'},
        '10': {'name': 'Аланья', 'code': 'GZP'}
    }

    # Выбор направления
    print("Доступные города отправления:")
    for key, city in cities.items():
        print(f"{key}. {city['code']} - {city['name']}")

    while True:
        try:
            origin_choice = input("Выберите номер города отправления: ")
            origin = cities[origin_choice]['code']
            break
        except KeyError:
            print("Неверный выбор города отправления.")

    print("Доступные города назначения:")
    for key, city in cities.items():
        print(f"{key}. {city['code']} - {city['name']}")

    while True:
        try:
            destination_choice = input("Выберите номер города назначения: ")
            destination = cities[destination_choice]['code']
            break
        except KeyError:
            print("Неверный выбор города назначения.")

    if origin == destination:
        print("Город отправления и город назначения не могут совпадать.")
        exit(1)

    # Выбор даты начала поиска
    while True:
        start_date_input = input("Введите дату начала поиска (например, 01.01.2024) или нажмите Enter для использования сегодняшней даты: ")
        if start_date_input == "":
            start_date = datetime.now()
            break
        else:
            try:
                start_date = datetime.strptime(start_date_input, '%d.%m.%Y')
                break
            except ValueError:
                print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ, (например, 01.01.2024)")

    # Выбор количества дней
    while True:
        try:
            days = int(input("Выберите период поиска (в днях): "))
            if days > 0:
                break
            else:
                print("Количество дней должно быть больше 0.")
        except ValueError:
            print("Пожалуйста, введите число.")

    tickets, origin_city_name, destination_city_name = get_cheapest_tickets(origin, destination, start_date, days)

    # Находим самый дешевый билет
    if tickets:
        cheapest_ticket = min(tickets, key=lambda x: x['price'])

        # Выводим информацию о самом дешевом билете
        print(f"\nСамый дешевый билет по направлению {origin_city_name} - {destination_city_name} c {start_date.strftime('%d.%m.%Y')} на {days} дн. вперед:")
        print(f"Дата: {cheapest_ticket['date']}, Цена: {cheapest_ticket['price']}₽, "
                f"Вылет: {cheapest_ticket['departure_time']}, Прилет: {cheapest_ticket['arrival_time']}")

        # Сохраняем все результаты в CSV файл
        with open('cheapest_tickets.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['date', 'price', 'departure_time', 'arrival_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ticket in tickets:
                writer.writerow(ticket)
        print("\nРезультаты сохранены в файл cheapest_tickets.csv")
    else:
        print("Билеты не найдены.")