#https://date.nager.at

import requests

def get_holidays(country_code, year):

    api_url = f'https://date.nager.at/api/v3/publicholidays/{year}/{country_code}'

    try:
        response = requests.get(api_url)
        holidays_data = response.json()

        if response.status_code == 200:
            if holidays_data:
                print(f'Праздники в {country_code} в {year} году')
                for holday in holidays_data:
                    print("Дата - ", holday['date'])
                    print("Название - ", holday['name'])
                    print("Локальное название - ", holday['localName'])
                    print("----------------------------------------------")
            else:
                print(f'Нет данных о праздниках')
                #holiday['date']
    except Exception as e:
        print(e)


country_code = input("Введите код страны: ")
year = int(input("Введите год: "))

get_holidays(country_code, year)