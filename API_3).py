#https://valorant-api.com/
#https://docs.opendota.com/
#https://api.opendota.com/api/

import requests
def get_valorant_data(endpoint):
    base_url = "https://valorant-api.com/v1/"
    api_url = f'{base_url}-{endpoint}&language=ru-RU'

    try:
        response = requests.get(api_url)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            return None
    except Exception as e:
        print(e)
        return None

agent_data = get_valorant_data("agents")
if agent_data:
    print("Персонажи в Valorant: ")
    for agent in agent_data['data']:
        if agent['role']:
            print("Имя: ", agent['displayName'])
            print("Роль: ", agent['role']['displayName'])
skins_data = get_valorant_data("weapons/skins")
if skins_data:
    print("\n Скины в валоранте")
    for skin in skins_data['data']:
        print("Оружие: ", skin['displayName'], " - ", skin['displayIcon'])