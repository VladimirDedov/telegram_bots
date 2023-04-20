import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = '6032194699:AAE2uXi34adqOIjYoC99MJTXRUme19cv0E4'
TEXT: str = 'Ура! Классный апдейт!'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            print(cat_response)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['link']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1