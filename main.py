#https://catfact.ninja
#https://catfact.ninja/breeds
#https://catfact.ninja/fact
#https://catfact.ninja/facts

import requests


def send_request(url):
    response = requests.get(url)
    # print(response.headers)
    # print(response.content)
    if response.status_code == 200:
        print("Преобразованные данные: ", response.json())

        data = response.json()
        print("Полученные данные")
        for key, value in data.items():
            print(f'Ключ {key}, Значение: {value}')
    else:
        print(f'Ошибка: {response.status_code} - {response.text}')

# send_request("https://catfact.ninja/fact")

print("1 - Список хлеба")
print("2 - Случайный факт")
print("3 - Список фактов")

choose = int(input("Выберите запрос"))

if choose == 1:
    send_request("https://catfact.ninja/breeds")
elif choose == 2:
    send_request("")
elif choose == 3:
    send_request("")
else:
    print("Нет такого выбора")