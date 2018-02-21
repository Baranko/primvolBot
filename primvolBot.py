import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30): #функция для получения всех обновлений
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset} #параметры - offset - для сдвига, пометки уже просмотренных обновлений
        resp = requests.get(self.api_url + method, params) #к строке запроса прибавляется getUpdates
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text): #функция отправки сообщения. На вход - id-чата и текст
        params = {'chat_id':chat_id, 'text': text} #формируем параметры сообщения - id-чата и само сообщение
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params) #используем метод пост для отправки сообщения
        return resp

    def get_last_update(self): #функция получения последнего объекта
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update


def main():
    greet_bot = BotHandler('504179513:AAEJT5PbCxOXwRJOjgHrTAAc9n4fQ54Tl-A')
    greetings = ('здравствуй', 'привет', 'здорово', 'хай')
    now = datetime.datetime.now()
    new_offset = None
    hour = now.hour
    
    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        if isinstance(last_update, list): 
            last_update_id = last_update[-1]['update_id'] 
        elif last_update == None: 
            continue 
        else: 
            last_update_id = last_update['update_id']
            
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and  6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))

        if last_chat_text.lower() in greetings and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Доброе день, {}'.format(last_chat_name))

        if last_chat_text.lower() in greetings and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Доброе вечер, {}'.format(last_chat_name))

        new_offset = last_update_id + 1

        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

