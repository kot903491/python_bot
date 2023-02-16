import requests
import time
import match

API_URL:str = 'https://api.telegram.org/bot'
BOT_TOKEN:str = '5849642826:AAFOvnJTbn1sDvVO7cT4HcV1K8Lxo08cIk8'
TEXT:str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 30

API_CATS_URL: str = 'https://aws.random.cat/meow'
ERROR_TEXT:str ='Здесь должна быть картинка :('


offset: int = -2
counter: int = 0
chat_id: int

api_photo:str
api_response = requests.Response
text:str
photo_link:str


while counter < MAX_COUNTER:
    b:bool=False
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            text = result['message']['text']
            
            match text:
                case "/help":
                    api_photo = 'https://aws.random.cat/meow'
                    api_response = requests.get(api_photo)   
                    if api_response.status_code==200:
                        photo_link = api_response.json()['file']
                        b=True
                case "/ahtung":
                    api_photo = 'https://random.dog/woof.json'
                    api_response = requests.get(api_photo)   
                    if api_response.status_code==200:
                        photo_link = api_response.json()['url']
                        b=True
                case "/valera":
                    api_photo = 'https://randomfox.ca/floof/'
                    api_response = requests.get(api_photo)   
                    if api_response.status_code==200:
                        photo_link = api_response.json()['image']
                        b=True
                case _:
                    pass
                    
            if b:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={photo_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
                            
                                
            

    time.sleep(1)
    counter += 1