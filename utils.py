import random
import os
import json
import dotenv
import ollama


def create_advertising():
    adds = [
        '''
        Привет! ⭐️
        Возможно, ты уже слышал о нашей бесплатной дебетовой карте, но знаешь ли ты об остальных её плюсах?
        С ней ты можешь получать кешбэк рублями до 25%, совершать платежи и переводы без комиссии и получать выгодные сделки у партнеров!
        Скорей оформляй её по ссылке 👉 https://www.vtb.ru/personal/karty/debetovye/multikarta/
        ''',
        '''
        Салют! Хотела узнать, а ты уже завёл свой накопительный счет 'Сейф'?
        Оказывается, его можно открыть всего лишь с 1к рублей на счету, и ты будешь получать от 5% процентов ежемесячно от суммы на счету!
        Эх, если бы дупло в дереве также работало...
        '''
    ]

    return random.choice(adds)


def get_ai_response(message):
    prompt = 'Ты виртуальный ассистент ВТБ Банка, его маскот - белка. Твои ответы не должны быть длинными, максимум 2-3 развернутых предложения. Отвечай на русском языке.'
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': prompt
        },
        {
            'role': 'user',
            'content': message,
        },
    ])
    return response['message']['content']
