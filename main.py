import dotenv
import os
import random
from datetime import datetime
import time
import threading

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from db import Database
from utils import create_advertising, get_ai_response


class VtbBot:
    def __init__(self):
        dotenv.load_dotenv()
        self.vk = vk_api.VkApi(token=os.getenv('API_KEY'))
        self.longpoll = VkLongPoll(self.vk)
        self.database = Database()
        self.send_interval = 60 # интервал рассылки в секундах
        self.last_send_time = 0

    def send_message(self, user_id, message):
        random_id = random.randint(1, 2e10)
        self.vk.method('messages.send', {'peer_id': user_id, 'message': message, 'random_id': random_id})

    def send_mass_message(self, message):
        for user_id in self.database.get_all_records():
            if 'vk_id' in user_id:
                self.send_message(user_id['vk_id'], message)

    def handle_messages(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text.lower()
                self.database.add_record(data={
                    'vk_id': event.user_id
                })
                self.send_message(event.user_id, get_ai_response(message=text))

    def run(self):
        print(f'[{datetime.now()}]: Бот успешно запущен!')
        message_thread = threading.Thread(target=self.handle_messages)
        message_thread.start()

        while True:
            if time.time() - self.last_send_time >= self.send_interval:
                self.send_mass_message(create_advertising())
                self.last_send_time = time.time()
            time.sleep(1)


bot = VtbBot()
bot.run()
