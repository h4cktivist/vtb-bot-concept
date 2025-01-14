# Концепт чат-бота ВТБ для кейс-чемпионата


### Запуск

Установка зависимостей: `pip install -r requirements.txt`

Задание API ключа VK:
* Создать файл *.env* в корне проекта.
* Записать туда переменную `API_KEY` с ключом в формате `API_KEY=[ключ]`

Установка LLM локально:
* Скачать и установить приложение Ollama: [тык](https://ollama.com/)
* Установить модель llama3, используя консоль: `ollama pull llama3`

Старт бота: `python main.py`


### Конфигурация

* Данные хранятся в JSON базе данных `database.json`, которая автоматически создается после инициализации бота.
* Интервал для рассылки (60 секунд по умолчанию) можно изменить в файле `main.py`
```python
self.send_interval = [значение в секундах]
```
* Рекламные сообщения для рассылки добавляются в массив, хранящийся в переменной `adds` файла `utils.py`.
* Промпт с описанием "поведения" LLM (ИИ) можно изменять в переменной `prompt` файла `utils.py`.
